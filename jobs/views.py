from django.shortcuts import render
from .models import Job

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', {'jobs': jobs})

def boop(request):
    return render (request, 'jobs/boop.html')
