from django.contrib.messages.api import add_message, error
from django.contrib.messages.constants import ERROR
from django.db.models.expressions import Exists
from django.http import request
from django.shortcuts import redirect, render
from .models  import Data,Snippet
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SnippetForm
from donarapp import forms




# Create your views here.
def home(request):
    return render(request,'home.html')

def main(request):
    return render(request,'welcome.html')

def register(request):
    if request.method=="POST":
        usernames=request.POST['username']
        password=request.POST['password']
        con=request.POST['confirm_password']
        sex=request.POST['sex']
        address=request.POST['address']
        number=request.POST['number']
        s=User.objects.filter(username=usernames)
        
        if not s.exists():
            if password==con:
                User.objects.create_user(username=usernames,password=password).save()
                Data(username=usernames,address=address,phone_number=number,sex=sex).save()
                messages.add_message(request,messages.ERROR,"USER REGISTERED")
                return redirect('/')
            else:
                messages.add_message(request,messages.ERROR,"PASSWORD DOES NOT MATCH")
                return redirect('/')
        else:
            messages.add_message(request,messages.ERROR,"USERNAME EXISTS")
            return redirect('/')
    else:
        return render(request,'home.html')


def logins(request):
    username=request.POST['user']
    password=request.POST['pass']
    user=authenticate(username=username,password=password)
    if user :
        login(request,user)
        return render(request,'welcome.html')
    else:
        messages.add_message(request,messages.ERROR,"INCORRECT CREDENTIALS")
        return redirect('/')

def logsout(request):
    logout(request)
    return redirect('/')



def donar(request): 
    form=SnippetForm()
    return render(request,'donar.html',{'form':form})



def complete(request):
    if request.method=="POST":
        form=SnippetForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('welcome')             
    else:
        form=SnippetForm()
        return render(request,'donar.html',{'form':form})

 
def search(request):
    datas=Snippet.objects.all()
    context={'datas':datas}
    return render(request,'search.html',context)


def search_value(request):
    if request.method=="POST":
        blood_group=request.POST['name'].lower()
        address=request.POST['address'].lower()
        datas=Snippet.objects.filter(blood_group=blood_group,city=address)
        if datas is None:
            messages.add_message(request,messages.ERROR,"NO RESULT FOUND")
            return render(request,'search.html')
        else:
            context={'datas':datas}
            return render(request,'search.html',context)
    else:
        return redirect('/')

def account(request):
    current_user=request.user
    user_id=current_user.id
    print(user_id)
    g=User.objects.get(id=user_id)
    print(g.username)
    u=g.username
    t=Data.objects.get(username=u)
    print(t.username)
    return render(request,'account.html',{'t':t})

def address(request):
   
    return render(request,'address.html')

def address_return(request):
    current=request.user
    user_id=current.id
    n=User.objects.get(id=user_id)
    t=Data.objects.get(username=n.username)
    val=request.POST['address']
    t.address=val
    t.save()
    return redirect('account')
    
def phone(request):
    return render(request,'phone.html')

def phone_return(request):
    current=request.user
    user_id=current.id
    n=User.objects.get(id=user_id)
    t=Data.objects.get(username=n.username)
    val=request.POST['phone']
    t.phone_number=val
    t.save()
    return redirect('account')

