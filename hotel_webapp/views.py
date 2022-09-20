from django.http import HttpResponse
from django.shortcuts import render
from requests import request

def homePage(request):
    return render(request, "homepage.html")

def login(request):
    fn=login()
    data= {'form':fn}
    try:
        if request.method=="POST":
            n1= request.POST.get('staff name')
            n2= request.POST.get('Staff Address')
            n3= request.POST.get('Staff Pancard')
            n4= request.POST.get('Staff Aadhaar')
            n5= request.POST.get('Staff Phone Number')

            data={
                'form':fn,
                'n1':n1,
                'n2':n2,
                'n3':n3,
                'n4':n4,
                'n5':n5,

            }

    except:
        pass

    return render(request, "login.html", data)

def contact_us(request):
    return render(request, "contact_us.html")



def onlinebooking(request):
    fx=login()
    data= {'form':fx}
    try:
        if request.method=="POST":
            x1= request.POST.get('customer name')
            x2= request.POST.get('Customer Address')
            x4= request.POST.get('Customer Aadhaar No')
            x5= request.POST.get('Customer Phone No')
            
            
            data={
                'form':fx,
                'x1':x1,
                'x2':x2,
                'x4':x4,
                'x5':x5,
                
                



            }

    except:
        pass

    return render(request, "onlinebooking.html", data)

def rooms_suites(request):
    return render(request,"rooms_suites.html")