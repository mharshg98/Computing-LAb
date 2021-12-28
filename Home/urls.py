from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('',views.index ,name="index"),
     path('adminLogin',views.adminLogin ,name="adminLogin"),
     path('logout',views.logout ,name="logout"),
     path('addnotice',views.addnotice ,name="addnotice"),
     path('shownotices',views.shownotice ,name="shownotice"),
     path('deleteNoticeData',views.deletenotice ,name="deletenotice"),
     path('addStudent',views.addStudent ,name="addStudent"),
     path('showstudent',views.showstudent ,name="showstudent"),
     path('uploadhomeimage',views.uploadhomeimage ,name="uploadhomeimage"),
     path('deleteImageData',views.deleteImageData ,name="deleteImageData"),
]