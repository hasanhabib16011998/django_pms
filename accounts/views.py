from django.shortcuts import render
from django.views.generic import View
from projects.models import *
from tasks.models import *
from .models import *

# Create your views here.
class DashBoardView(View):
    def get(self, request, *args, **kwargs):
        context={}
        latest_projects = Project.objects.all()[:5]
        latest_tasks = Task.objects.all()[:5]
        latest_members = Profile.objects.all()
        context['latest_projects'] = latest_projects
        context['latest_tasks'] = latest_tasks
        context['latest_members'] = latest_members
        return render(request,"accounts/dashboard.html", context)
