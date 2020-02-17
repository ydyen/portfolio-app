from django.shortcuts import render

from .models import Job


def home(request):
    job = Job.objects.all()
    return render(request, 'job/job.html', {'jobs': job})