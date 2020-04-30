from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import UserInfo
from .forms import UserInfoForm
from django.utils import timezone
# Create your views here.
def index(request):
	#return HttpResponse("Hello World.")
	return render(request,'synerd.html',{})

# def register(request):
# 	return render(request,'joinus.html',{})


def member(request):
	query_results = UserInfo.objects.all()
	return render(request, 'members.html', locals())

def register(request):
    #form = UserInfoForm
    #return render(request, 'joinus_edit.html', {'form': form})
    query_results = UserInfo.objects.all()
    if request.method == "POST":
        form = UserInfoForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.governmentIDexpiredate = timezone.now()
            user.save()
            return render(request, 'members.html', locals())
    else:
        form = UserInfoForm()
    return render(request, 'joinus_edit.html', {'form': form})

 # if request.method == 'POST':
 #  r = requests.get('http://localhost:8000/api/services/', params=request.POST)
 # else:
 #  r = requests.get('http://localhost:8000/api/services/', params=request.GET)	 

 #  if r.status_code == 200:
 #   return HttpResponse(r.text)
 #  else:    
 #   return HttpResponse('Could not save data')
	#return render(request,'members.html',{})