from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.
# 
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
             send_mail('Registratioon',"Succefully Registration is Done",'shashivardhan072@gmail.com',
                      [MUFDO.email],fail_silently=False)
             return HttpResponse('Regsitration is Susssessfulll')
        else:
            return HttpResponse('Not valid')


           
    return render(request,'registration.html',d)


    
    
    

    
    

