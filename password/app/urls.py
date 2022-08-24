from django.urls import path
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('employeewaitlist/', views.Employeewaitlist.as_view()),
    path('employeewaitlist/<str:pk>/', views.EmployeeDetailEdit.as_view()),
    path('signupuser/', views.Signupuser.as_view()),
    path('save-country/', views.Savecountry.as_view()),
    path('save-state/', views.Savestate.as_view()),
    path('check-userwait/', views.Checkuserwait.as_view()),
    path('save-userwait/', views.Saveuserwait.as_view()),
    path('loginuser/', views.Loginuser.as_view()),

]