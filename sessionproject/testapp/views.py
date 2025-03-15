from django.shortcuts import render
from testapp.forms import LoginForm

def home_view(request):
    form = LoginForm()
    return render(request,'testapp/home.html',{'form':form})

def date_time_view(request):
    name = request.GET['name']
    response = render(request,'testapp/datetime.html',{'name':name})
    response.set_cookie('name',name)
    return response

 