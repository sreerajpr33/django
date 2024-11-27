from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def ins_home(req):
    data=Inscourses.objects.all()[:3]
    return render(req,'index.html',{'courses':data})

def about(req):
    return render(req,'about.html')

def contactus(req):
    return render(req,'contact.html')

def courses(req):
    data=Inscourses.objects.all()
    return render(req,'course.html',{'courses':data})

def sendmessage(req):
     if req.method=='POST':
          name=req.POST['name']
          email=req.POST['email']
          message=req.POST['message']
          data=Message.objects.create(name=name,email=email,message=message)
          data.save()
          return redirect(contactus)
     else:
          return render(req,'contact.html')
     
def details(req,c_id):
    data=Inscourses.objects.get(pk=c_id)
    return render(req,'details.html',{'data':data})
