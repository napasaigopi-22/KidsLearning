from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, Template



# Create your views here.
def home(req):
    return render(req,"HTML/home.html",{"lavada":['lavadalo','manchivipettara']})