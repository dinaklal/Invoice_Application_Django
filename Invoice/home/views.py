from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from login.models import Sites
from django.contrib import messages
# Create your views here.


def home(request):
    sites= Sites.objects.all()
    return render(request,'home.html',{'sites':sites})
def logout(request):
    auth.logout(request)
    return redirect('/')
def add_site(request):
    if request.method == 'POST':
        name = request.POST['name']

        price = request.POST['price']
        desc = request.POST['desc']
        if Sites.objects.filter(name=name).exists():
            messages.error(request,'duplicate')
            return redirect('add_site')
        else:
            ob=Sites(name=name,Unit_price=price,Description=desc)
            ob.save()
            messages.info(request,'done')
            return redirect('add_site')
    else:
        return render(request,'add_site.html')
def view_site(request):
    sites= Sites.objects.all()
    return render(request,'view_site.html',{'sites':sites})
def process(request):
    post_data = dict(request.POST.lists())
    post_data.pop('csrfmiddlewaretoken',None)
    print(post_data)
    print(request.POST['num1'])
    return render(request,'invoice_added.html',{'data':post_data})