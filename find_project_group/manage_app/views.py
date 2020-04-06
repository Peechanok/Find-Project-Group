
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.models import Group, User
from django.db import IntegrityError
from django.forms import models
from django.http import HttpResponse, request
from django.shortcuts import redirect, render
from django.urls.base import is_valid_path

from .models import Student,Course

def selectCouse(request):
    coursall = Course.objects.all()
    return render(request, 'manage_app/course.html',context={
        'coursall': coursall,}
    )



def viewaddCourse(request):
    course = Course.objects.all()

    return render(request, 'manage_app/add_course.html',context={'course':course})


@login_required   
@permission_required('manage_app.add_course')
def addCourse(request):
    msg = ''
    
    if request.method == 'POST':
        course = Course.objects.create(
            
            name=request.POST.get('name'),
            desc=request.POST.get('desc'),
           
        )
        
        msg = 'Successfully create new name courese'
    else:
        course = Course.objects.none()

    context = {
       
       'course':course,
        'msg': msg
    }

    return render(request, 'manage_app/add_course.html', context=context)
@login_required   
@permission_required('manage_app.delete_course')
def viewCourse(request):
    course = Course.objects.all()

    return render(request, 'manage_app/view_course.html',context={'course':course})

def deleteCourse(request,course_id):
    """
        ลบข้อมูล course โดยลบข้อมูลที่มี id = course_id
    """
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect(to='view_course')
 