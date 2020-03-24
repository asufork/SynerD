from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	#return HttpResponse("Hello World.")
	return render(request,'synerd.html',{})

def register(request):
	return render(request,'joinus.html',{})

