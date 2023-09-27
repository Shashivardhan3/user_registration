from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)
    return render(request,'home.html')


def registration(request):
    USFO=UserForm()
    PFO=ProfileForm()
    d={'USFO':USFO,'PFO':PFO}
    if request.method=='POST' and request.FILES:
        UFDO=UserForm(request.POST)
        PFDO=ProfileForm(request.POST,request.FILES)
        if UFDO.is_valid() and PFDO.is_valid():
             MUFDO=UFDO.save(commit=False)
             MUFDO.set_password(UFDO.cleaned_data['password'])
             MUFDO.save()

             MPFDO=PFDO.save(commit=False)
             MPFDO.username=MUFDO
             MPFDO.save()
             send_mail('Registration',"Succefully Registration is Done",'shashivardhan072@gmail.com',
                      [MUFDO.email],fail_silently=False)
             return HttpResponse('Regsitration is Successfulll')
        else:
            return HttpResponse('Not valid')


           
    return render(request,'registration.html',d)


def user_login(request):
    if request.method=="POST":
        username=request.POST['un']
        password=request.POST['pw']
        AUO=authenticate(username=username,password=password)
        if AUO and AUO.is_active():
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('login credentials are invalid')
    return render(request,'user_login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
    

    
    

