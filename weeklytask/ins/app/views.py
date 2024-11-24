from django.shortcuts import render

# Create your views here.
def ins_home(req):
    return render(req,'index.html')

def about(req):
    return render(req,'about.html')

def contactus(req):
    return render(req,'contact.html')

def courses(req):
    return render(req,'course.html')