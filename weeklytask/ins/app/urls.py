from django.urls import path
from . import views

urlpatterns = [
    path('',views.ins_home),
    path('aboutus',views.about),
    path('contactus',views.contactus),
    path('course',views.courses),
    path('smessage',views.sendmessage),
    path('details/<c_id>',views.details),
]