from django.shortcuts import render,redirect
from.models import*
# Create your views here.
std=[]
def home(req):
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        # std.append({'roll_no':roll,'name':name,'age':age})
        data=student.objects.create(name_no=roll,name=name,age=age)
        return redirect(home)
    else:
        data=student.objects.all()
        return render(req,'home.html',{'student':data})
    
def edt_std(req,id):
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        student.objects.filter(pk=id).update(name_no=roll,name=name,age=age)
        return redirect(home)
    else:
        data=student.objects.get(pk=id)
        return render(req,'edit.html',{'data':data})