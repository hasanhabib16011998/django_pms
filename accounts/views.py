from django.shortcuts import render
from django.views.generic import View
from projects.models import *

# Create your views here.
class DashBoardView(View):
    def get(self, request, *args, **kwargs):
        context={}
        latest_projects = Project.objects.all()[:5]
        context['latest_projects'] = latest_projects
        return render(request,"accounts/dashboard.html", context)
