from django.contrib import admin
from django.urls import path
from .views import *

app_name='accounts'

urlpatterns = [
    path('', DashBoardView.as_view(), name='dashboard'),
    path('members', MembersListView.as_view(), name="members-list"),
    path('register/', RegisterView, name='register'),

]