from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    data={
        'title':'new Home',
        'bdata':'Welcome to my site',
        'clist':['php','java','django'],
        'std_details':[{'name':'rama','phone':'92472'},
                       {'name':'subba','phone':'630453'}],
        'number':[10,20,30,40,50]
    }
    return render(request,"index.html",data)
def aboutus(request):
    return render(request,'index.html')
def course(request):
    return HttpResponse("this are the courses available")
def details(request,details):
    return HttpResponse(details)