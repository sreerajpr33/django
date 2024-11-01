from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
# Create your views here.
def fun1(req):
    return HttpResponse("hey !")
def fun2(req):
    return render(req,'demo.html')
def home(req):
    return render(req,'home.html')
def about(req):
    return render(req,'about.html')
def contact(req):
    return render(req,'contact.html')

l=[]
def fun3(req):
    if req.method=='POST':
        name=req.POST['name']
        age=req.POST['age']
        print(name,age)
        l.append({'name':name,'age':age})
        print(l)
        return redirect(fun3)
    else:
        return render(req,'home.html')
def fun4(req):
    return render(req,'about.html')


l=[{'name':'abhishek','age':'90'},{'name':'aby','age':'90'}]
def display(req):
    a='welcome'
    return render(req,'display.html',{'data':l,'data1':a})
    
def  add_dtls(req):
    if req.method=='POST':
        name=req.POST['name']
        age=req.POST['age']
        print(name,age)
        l.append({'name':name,'age':age})
        return redirect(display)
    else:
        return render(req,'add.html')