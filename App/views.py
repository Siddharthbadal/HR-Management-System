from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_protect
from .forms import CandidateForm
from .models import Candidate
from django.http import HttpResponseRedirect
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control  # destroyes session after logout
from django.core.paginator import Paginator
from django.db.models import Q 
from django.db.models.functions import Concat 
from django.db.models import Value as Val 
import pdfkit 

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
        context ={
            'candidates': filter
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
    context = {'candidates': all_candidates}
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




# export to pdf 
@csrf_protect
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def download_candidate_pdf(request, id):
    c = Candidate.objects.get(pk=id)
    cookies = request.COOKIES
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
        "enable-local-file-access": "",
        'cookie': [
            ('csrftoken', cookies['csrftoken']),
            ('sessionid', cookies['sessionid'])
        ]
    }
    # pass live url 
    
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    pdf = pdfkit.from_url('http://127.0.0.1:8000/'+str(c.id), False, options=options, configuration=config)
    res = HttpResponse(pdf, content_type="application/pdf")
    res['content-disposition'] = 'attachment; filename=candidate.pdf'
    return res 

