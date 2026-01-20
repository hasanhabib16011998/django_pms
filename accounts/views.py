from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class DashBoardView(View):
    def get(self, request, *args, **kwargs):
        context={}
        context["name"] = "Hasan"
        context["email"] = "hasan@vertical-innovations.com"
        return render(request,"accounts/dashboard.html", context)
