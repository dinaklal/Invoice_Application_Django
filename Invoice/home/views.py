from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from login.models import Sites
from home.models import Invoice,Sales
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
    total= post_data['total_amount'][0]
    discount = post_data['discount'][0]
    total_units=  post_data['tot_units'][0]
    customer = post_data['customer'][0]
    contact = post_data['contact'][0]
    address = post_data['address'][0]
    #print(total)    
    ob = Invoice(customer=customer,address=address,contact=contact,discount=discount,total_price=total,total_units=total_units)
    ob.save()
    inv_id = Invoice.objects.latest('id').id
    if discount == '':
        discount = "0"
    invoice  = {'name':customer,'address':address,'id':inv_id,'discount':float(discount),'contact':contact,'total':total,'tot_units':total_units,'to':float(total)-float(discount)}   
    sale = []
    sn={}
    i=1
    for key in post_data:
        
        if key.startswith('selid'):
            site_id = post_data[key][0]
            s= Sites.objects.get(id=site_id)
            sn['name']=s.name
            sn['uprice']=s.Unit_price
        if key.startswith('sel1id'):
            units_load= post_data[key][0]
            sn['uload']=units_load
        if key.startswith('lodid'):
            no_loads = post_data[key][0]
            sn['loads']=no_loads
        if key.startswith('untid'):
            tot_units = post_data[key][0]
            sn['units']=tot_units
        if key.startswith('totid'):
            sn['sino']=i
            i=i+1
            tot_price = post_data[key][0]
            sn['price']=tot_price
            
            sale.append(sn)
            sn={}
            ob= Sales(inv_id=inv_id,site_id=site_id,units_load=units_load,no_loads=no_loads,tot_units=tot_units,tot_price=tot_price)
            ob.save()
        
    
    print(sn)
    return render(request,'invoice_added.html',{'invoice':invoice,'sales':sale})