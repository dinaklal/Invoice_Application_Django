from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User
# Create your views here.
def login(request):
    users = User.objects.all()
    return render(request,'index.html',{'Users':users,'name':'Mughal Invoice'})
