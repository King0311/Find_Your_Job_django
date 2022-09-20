from email import message
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import *
from django.urls import reverse
# Create your views here.


def homepage(request):
    return render(request, "home.html")


def signup(request):
    if (request.method == "POST"):
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if (password1 == password2):
            if User.objects.filter(username=username).exists():
                messages.info(request, "username is already taken")
                return redirect("signup")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "This email is already resigtered")
                return redirect("signup")
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                    email=email
                )
                user.save()
                return redirect("login")
        else:
            messages.info(request, "Password doesn't match")
            return redirect("signup")
    else:
        return render(request, "signup.html")


def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/") 
        else:
            messages.info(request,"Your are not our user or something may be wrong. Please try again later.")
            return redirect("login")
    else:
        return render(request, "login.html")


def logout(request):
    auth.logout(request)
    return redirect("/")


def hr_seeker(request):
    lgin=request.user
    user=User.objects.get(username=lgin)
    form=hr_profile_form()
    if request.method == 'POST':
        form=hr_profile_form(request.POST)
        if form.is_valid():
            data=form.save()
            return data
        else:
            pass
    else:
        form=hr_profile_form(instance=user)
    return render(request,"hr_seeker.html",{'form':form,'lgin':lgin})


def seeker(request):
    lgin=request.user
    user=User.objects.get(username=lgin)
    form2=seeker_porfile_form()
    if request.method == 'POST':
        form2=seeker_porfile_form(request.POST)
        # if seeker_profile.objects.filter(username=lgin).exists():
        #     return redirect("seeker")
        if form2.is_valid():
            data2=form2.save()
            return data2.profession.lower()
        else:
            pass
    else:
        form2=seeker_porfile_form(instance=user)  
    return render(request,"seeker.html",{'form2':form2,'lgin':lgin})


def jobs(request,pk):
    jobs=hr_profile.objects.all()
    seekers=seeker_profile.objects.all()
    datas=seeker(request)
    return render(request,"jobs.html",{'pk':pk,'jobs':jobs,'datas':datas,'seekers':seekers})

def giver(request,fk):
    useless=hr_seeker(request)
    jobs=hr_profile.objects.all()
    hr=hr_profile.objects.filter(username=fk).first()
    return render(request,"job_giver.html",{'fk':fk,'jobs':jobs,'hr':hr})