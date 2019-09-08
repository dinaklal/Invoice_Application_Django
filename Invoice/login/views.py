from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.
def login(request):
    u1= User()
    return render(request,'index.html',{'name':'Mughals Invoice'})
