from django.shortcuts import render
from .forms import CandidateForm
from .models import Candidate
from django.http import HttpResponseRedirect
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control  # destroyes session after logout

def home(request):
    return render(request, 'home.html')


# registration
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
@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def backend(request):
    candidates = Candidate.objects.all()
    context = {'candidates_data': candidates}
    return render(request, 'backend.html', context)


@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def candidate(request, id):
    candidate = Candidate.objects.get(pk=id)
    form = CandidateForm(instance=candidate)

    # read only cadidates fields for candidate.html
    readonly_fields = ['experience','job','firstname', 'lastname', 'email', 'gender', 'birthdate', 'mobile', 'city', 'education','position','salary','cloud', 'languages', 'frameworks','databases','other_skills','message','profile_image', 'file', 'course', 'institution', 'course_started', 'course_finished', 'course_details', 'course_mode',
        'company', 'role', 'started_at', 'ended_at', 'notice_period', 'about_role', 'hybrid_office', 'still_working','linkedin', 'github', 'project', 'portfolio']

    for field in readonly_fields:
        form.fields[field].disabled = True
        
        # disable upload fields
        form.fields['file'].widget.attrs.update({'style':'display:None;'})
        form.fields['profile_image'].widget.attrs.update({'style':'display:None;'})

    context = {'form': form}
    return render(request, 'candidate.html', context)