from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .forms import CandidateForm, EmailForm, Chat_candidatedForm
from .models import Candidate, Email, Chat_candidate
from django.http import HttpResponseRedirect
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control  # destroyes session after logout
from django.core.paginator import Paginator
from django.db.models import Q 
from django.db.models.functions import Concat 
from django.db.models import Value as Val 
from django.core.mail import EmailMessage
from django.contrib.auth.models import User 


def home(request):
    return render(request, 'home.html')


# registration
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)        
        print(form.is_valid())
    
        if form.is_valid():
            print("form valid")
            form.save()
            print("form saved")
            messages.success(request, "Registered Successfully")
            return HttpResponseRedirect('/')
        else:
            return render(request, "register.html", {'form':form})
    else:
        form = CandidateForm()
        return render(request, "register.html", {'form':form})
    


# backend
@csrf_protect
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def backend(request):
    # filter by job and experience
    if request.method == 'POST':
        job= request.POST.get('job')
        experience= request.POST.get('experience')
        filter = Candidate.objects.filter(Q(job=job) | Q(experience=experience) )
        total = Candidate.objects.all().count()
        frontend = Candidate.objects.filter(job="FRE-01").count()
        backend = Candidate.objects.filter(job="BAC-01").count()
        fullstack = Candidate.objects.filter(job="SDE-01").count()
        context ={
            'candidates': filter,
            'total': total,
            'frontend': frontend,
            'backend': backend,
            'fullstack': fullstack 
        }

        return render(request, 'backend.html', context)
    elif 'q' in request.GET:
        q = request.GET['q']
        candidates_list = Candidate.objects.annotate(name=Concat('firstname',Val(' '),'lastname')).filter(Q(name__icontains=q) | Q(firstname__icontains=q) | Q(lastname__icontains=q) | Q(created_at__icontains=q) | Q(email__icontains=q) | Q(mobile__icontains=q)|Q(gender__icontains=q)).order_by('-created_at')

    else:
        candidates_list = Candidate.objects.all().order_by('-created_at')
    paginator = Paginator(candidates_list, 5)   
    page_number = request.GET.get('page') 
    all_candidates = paginator.get_page(page_number)
    
    total = Candidate.objects.all().count()
    frontend = Candidate.objects.filter(job="FRE-01").count()
    backend = Candidate.objects.filter(job="BAC-01").count()
    fullstack = Candidate.objects.filter(job="SDE-01").count()


    context = {
                'candidates': all_candidates,
                'total': total,
                'frontend': frontend,
                'backend': backend,
                'fullstack': fullstack            
            }
    return render(request, 'backend.html', context)



@csrf_protect
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def candidate(request, id):
    candidate = Candidate.objects.get(pk=id)
    context = {
        'candidate':candidate
    }
    return render(request, 'candidate.html', context)



@csrf_protect
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def delete_candidate(request, id):
    candidate = Candidate.objects.get(pk=id)
    candidate.delete()
    messages.success(request, "Candidate deleted successfully!")
    return HttpResponseRedirect('/candidates')



@csrf_protect
def email(request):
    if request.method == 'POST':
        to_db= Email(
            status = request.POST.get('status'),
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            subject = request.POST.get('subject'),
            message = request.POST.get('message'),
            employee = request.POST.get('employee'),
        )
        print(Email)
        to_db.save()

        form = EmailForm(request.POST)
        company = "HRM"
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            mail = EmailMessage(subject, message, company, [email])
            mail.send()
            messages.success(request, "email sent successfully")
            return HttpResponseRedirect("/candidates")
        else:
            form = EmailForm()
            return render(request, {'form': form})



# simple messaging service among support staff and admin
@csrf_protect
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def chat_candidate(request, id):
    candidate = Candidate.objects.get(pk=id)
    chat_candidate = Chat_candidate.objects.all().order_by('-date_time')
    list_users = User.objects.all()
    form = Chat_candidatedForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('chat_candidate', id=candidate.id)
    context = {
        "form":form,
        "chat_candidate": chat_candidate,
        "list_users": list_users,
        "candidate":candidate
    }

    return render(request, 'chat_candidate.html', context)




