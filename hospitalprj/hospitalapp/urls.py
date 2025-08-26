from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path("list_department/", views.list_department, name="list_department"),
    path("add_department/", views.add_department, name="add_department"),
    path("list_doctor/", views.list_doctor, name="list_doctor"),
    path("add_doctor/", views.add_doctor, name="add_doctor"),
    path("list_patient/", views.list_patient, name="list_patient"),
    path("add_patient/", views.add_patient, name="add_patient"),
    path("list_time/", views.list_time, name="list_time"),
    path("add_time/", views.add_time, name="add_time"),
    path("list_appointment/", views.list_appointment, name="list_appointment"),
    path("add_appointment/", views.add_appointment, name="add_appointment"),
    path("get_doctors_by_department/", views.get_doctors_by_department, name="get_doctors_by_department"),
    path("get_available_hours", views.get_available_hours, name="get_available_hours"),
 

]