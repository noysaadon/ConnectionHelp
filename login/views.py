from django.core.mail import EmailMessage, send_mail
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from mysite import settings
from .models import User
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes ,force_str
from .token import generate_token
from volnteer import *


def home(request):
    return render(request,'login/index.html')


def signup(request): 
    if request.method =='POST':
        username = request.POST.get('username','')
        fullname = request.POST.get('fullname','')
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        pass2 = request.POST.get('pass2')
    

        if User.objects.filter(username=username):
            messages.error(request , "Username is already exsit , please try another username")

        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('/signin')

        if password != pass2:
            messages.error(request, "The passwords didn't match")

        if not username.isalnum():
            messages.error(request, "Username must be Alpa-Numeric")


        user = User(username=username,fullname=fullname,email=email,password=password)
        user.is_active = False
        name = user.fullname
        user.save()

        messages.success(request, "Your account has been succssefuly created. \n We have sent you a confirmation email, plese confirm your email in to activate your account")

        #Welcome Email to send

        subject="Welcome to ConnectionHelp! Here we are do good things(:"
        message="Hello " + user.fullname + " !! \n" + "wellcome to ConnectionHelp! \n Thank you for visiting our page, please confirm your email address in order to activate your account. \n\n Thank you, \n Noy Saadon"
        from_email = settings.EMAIL_HOST_USER
        to_list= [user.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        #Confirmation Email

        current_site = get_current_site(request)
        email_subject ="Confirm your email @ Connectionhelp Login!"
        message2 = render_to_string('login/email_confirmation.html',
        {
            'name' : user.fullname,
            'domain' : current_site.domain,
            'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
            'token' : generate_token.make_token(user),
        })

        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [user.email],
        )
        email.fail_silently =True
        email.send()

        return redirect('signin')
    
    return render(request,'login/signup.html') 


def signin(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('volnteer_charity')

        else:
            messages.error(request,"Somthing not match")
            return redirect('/')

    return render(request, 'login/signin.html')
    #return render(request,'volnteerandcharity/volnteercharity.html')


def signout(request):
    logout(request)
    messages.success(request, "Logged out successfuly!")
    return redirect('/')


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if (user is not None and generate_token.check_token(user, token)):
        user.is_active = True
        user.save()
        #login(request, user)
        return redirect('/')
    else:
        return render(request, 'login/activation_failed.html')