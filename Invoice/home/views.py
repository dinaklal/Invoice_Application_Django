from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from login.models import Sites
from home.models import Invoice,Sales
from django.contrib import messages
from datetime import datetime
from home.utils import render_to_pdf #created in step 4
from django.views.generic import View
from django.http import HttpResponse
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
    date=post_data['date'][0]
    date = datetime.strptime(date, "%Y/%m/%d")
    #print(total)    
    ob = Invoice(customer=customer,address=address,contact=contact,discount=discount,total_price=total,total_units=total_units,date=date)
    ob.save()
    inv_id = Invoice.objects.latest('id').id
    if discount == '':
        discount = "0"
    invoice  = {'date':date,'name':customer,'address':address,'id':inv_id,'discount':float(discount),'contact':contact,'total':total,'tot_units':total_units,'to':float(total)+float(discount)}   
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

def GeneratePdf(request):
        get_data = dict(request.GET.lists())
        id=get_data['inv_id'][0]
        invoice = Invoice.objects.get(id=id)
        sales= list(Sales.objects.filter(inv_id=id))
        sal = []
        sn={}
        i=1
        for sale in sales:
            s= Sites.objects.get(id=sale.site_id)
            sn['name']=s.name
            sn['uprice']=s.Unit_price
            sn['uload']=sale.units_load
            sn['loads']=sale.no_loads
            sn['units']=sale.tot_units
            sn['sino']=i
            i=i+1
            sn['price']=sale.tot_price
            
            sal.append(sn)
            sn={}
        if invoice.discount == '':
            invoice.discount = "0"
        to=float(invoice.total_price)+float(invoice.discount)
        pdf = render_to_pdf('invoice.html',{ 'invoice':invoice,'sales':sal,'to':to})
        return HttpResponse(pdf, content_type='application/pdf')