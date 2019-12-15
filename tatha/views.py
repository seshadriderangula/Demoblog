from django.core.serializers import json
from django.shortcuts import render
import requests,json
from .models import Contact,Register,Send
# Create your views here.
def index(request):
        return render(request, "tatha/index.html")
def contact(request):
    if request.method == 'POST':
       email = request.POST.get('email')
       subject = request.POST.get('subject')
       message = request.POST.get('message')
       c = Contact(email=email, subject=subject, message=message)
       c.save()
       return render(request, "tatha/thank.html",{"email":email})
    else:
       return render(request, "tatha/contact.html")

def send(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        d = Send(email=email,password=password)
        d.save()
        return render(request,"tatha/register.html",{"emial":email})
    else:
        return render(request,"tatha/send.html")


def portfolia(request):
    return render(request,"tatha/portfolia.html")

def register(request):
    if request.method == 'POST':
        Fname = request.POST.get('Fname')
        Lname = request.POST.get('Lname')
        username = request.POST.get('username')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        c = Register(Fname=Fname,Lname=Lname,username=username,city=city,state=state,zip=zip,password="krishna")
        c.save()

        return render(request,'tatha/login.html',{"username":username})
    else:
        return render(request,'tatha/register.html')




