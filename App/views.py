from django.shortcuts import render
from .forms import CandidateForm
from django.http import HttpResponseRedirect
from django.contrib import messages 


def home(request):
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
            return render(request, "home.html", {'form':form})
    else:
        form = CandidateForm()
        return render(request, "home.html", {'form':form})