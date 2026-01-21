from django.shortcuts import render
from django.views.generic import View
from projects.models import *
from tasks.models import *
from notifications.models import *
from .models import *

# Create your views here.
class DashBoardView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
               

        if user.is_superuser:
            print("Superuser")
            latest_projects = Project.objects.all()
            latest_tasks = Task.objects.all()
            latest_members = Profile.objects.all()
            team_count = Team.objects.all().count()
        else:
            print("not superuser")
            latest_projects = Project.objects.for_user(user) 
            latest_tasks = Task.objects.for_user(user) 
            latest_members = Profile.objects.filter(
                user__teams__in=user.teams.all()
            ).distinct()
            team_count = user.teams.all().count()

        
        context = {}
        latest_notifications = user.notifications.unread(user)
        context["latest_notifications"] = latest_notifications[:3]
        context["notification_count"] = latest_notifications.count()
        context["latest_projects"] = latest_projects[:5]
        context["latest_project_count"] = latest_projects.count()
        context["projects_near_due_date"] = latest_projects.due_in_two_days_or_less()[:5]
        context["latest_task_count"] = latest_tasks.count()
        context["latest_tasks"] = latest_tasks
        context["latest_members"] = latest_members[:8]
        context["latest_member_count"] = latest_members.count()
        context["team_count"] = team_count
        context["header_text"] = "Dashboard"
        context["title"] = "Dashboard"
        return render(request, "accounts/dashboard.html", context)
