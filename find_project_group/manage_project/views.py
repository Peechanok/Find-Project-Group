import email
import profile
from builtins import object
from datetime import date, datetime
from threading import Event
from tokenize import group
from urllib import request
from webbrowser import get

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import Group, User
from django.db import IntegrityError
from django.forms import models
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls.base import is_valid_path

from manage_app.models import Student

# Create your views here.

@login_required
def home(request):
        
    return render(request, 'home.html',)





def my_login(request):
    context = {}

    if request.method == 'POST':
       
        username = request.POST.get('username')
        password = request.POST.get('password')
               
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('find_project_home')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = "Sorry! Username and Password didn't match, Please try again !!"

    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url
        

    return render(request, template_name='Loginindex.html', context=context)

@login_required

def my_logout(request):
    logout(request)
    return redirect('find_project_login')

def sign_in(request):
    """
        เพิ่มข้อมูล user / student ใหม่เข้าสู่ฐานข้อมูล
    """
    msg = ''

    if request.method == 'POST':
        user = User.objects.create_user(
            request.POST.get('username'),
            request.POST.get('email'),
            request.POST.get('password'),
            
        )
       
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        student = Student.objects.create(
            user=user,
            year=request.POST.get('year'),
            major=request.POST.get('major'),
            contect=request.POST.get('contect')
        )
        user.save()
        msge = 'Successfully create new student - username: %s' % (user.username)
    else:
        user = User.objects.none()

    context = {
        'student': user,
        'msge': msge
    }

    return render(request, 'Loginindex.html', context=context)


@login_required
def change_password(request):
    context = {}
    if request.method == 'POST':
        user = request.user
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # check that the passwords match
        if password1 == password2:
            user.set_password(password2)
            user.save()
            redirect('login')
        else:
           context['password1'] = password1
           context['password2'] = password2
           context['error'] = "Sorry! Password didn't match, Please try again !!"



        # reset password 

    return render(request, template_name='change_password.html', context=context)

@login_required
def update_profile(request,user_id):
    """
        Update ข้อมูลชั้นเรียนที่มี id = class_id
    """
    
    try:
        user = User.objects.get(pk=user_id)
        msg = ''
    except User.DoesNotExist:
        return redirect('find_ptoject_home')

    if request.method == 'POST':
        user.username=request.POST.get('username')
        user.email=request.POST.get('email')
        user.first_name=request.POST.get('first_name')
        user.last_name=request.POST.get('last_name')
        
        
        user.save()
        msg = 'Successfully ffupdate student - username: %s' % (user.username)
        
    context = {
        
        'msg': msg
    }

    return render(request, template_name='manage_app/home.html', context=context)


@login_required
def update_profile(request,user_id):
    """
        Update ข้อมูลนักเรียนที่มี id = user_id
    """
    
    try:
        user = User.objects.get(pk=user_id)
        msg = ''
    except User.DoesNotExist:
        return redirect('find_project_home')

    if request.method == 'POST':
        user.username=request.POST.get('username')
        user.first_name=request.POST.get('first_name')
        user.last_name=request.POST.get('last_name')
        try:
            user.student.year=request.POST.get('year')
            user.student.major=request.POST.get('major')
            user.student.contect=request.POST.get('contect')
        except Student.DoesNotExist:
            student = Student.objects.create(
            user=user,
            year=request.POST.get('year'),
            major=request.POST.get('major'),
            contect=request.POST.get('contect')
        )
        user.save()
        msg = 'Successfully update student - username: %s' % (user.username)
    
    context = {
        'student': user,
        'msg': msg
    }

    return render(request, 'update_profile.html', context=context)
    
@login_required   
@permission_required('manage_app.view_student')
def profile_user(request):
        

    return render(request, 'update_profile.html')
