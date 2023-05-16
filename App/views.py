from django.shortcuts import render
from .forms import CandidateForm
from django.http import HttpResponseRedirect
from django.contrib import messages 


def home(request):
    form = CandidateForm(request.POST or None)
    print("In form..")
    print(form.is_valid())
  
    if form.is_valid():
        print("form valid")
        form.save()
        print("form saved")
        messages.success(request, "Registered Successfully")
        return HttpResponseRedirect('/')
    context = {
        'form': form
    }
    return render(request, "home.html", context)