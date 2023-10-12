from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data={
        'title':'Home Page',
        'description':'This is home page',
        'celldata':[{'name':'Mohsin', 'phone':'03157527330'},
        {'name':'Mushtaq', 'phone':'03455833662'},
        {'name':'Ahsan', 'phone':'12345679'}]
    }
    return render(request, "index.html", data)

def about(request):
    return HttpResponse("About Us")

def course(request):
    return HttpResponse("Courses")


def coursedetails(request, courseid):
    return HttpResponse("You are watching <h1>"+courseid+"</h1>")