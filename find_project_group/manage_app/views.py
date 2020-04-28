
from builtins import object
from django.http import JsonResponse
from venv import create

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Count
from django.forms import models
from django.http import HttpResponse, JsonResponse, request
from django.shortcuts import redirect, render
from django.urls.base import is_valid_path

from rest_framework.decorators import api_view

from .forms import *
from .models import *
from .serializers import *

@login_required
def selectCouse(request):
    coursall = Course.objects.all()
    return render(request, 'manage_app/course.html',context={
        'coursall': coursall,}
    )



@login_required
@permission_required('auth.view_user')
def removepro_ex(request, student_id,pro_id):
    student = Student.objects.get(id=student_id)
    project_ex = Project_experience.objects.get(pk=pro_id)
    

    project_ex.delete()
    return redirect(to='view_pro_ex', student_id=student.id)

@login_required

def view_pro_ex(request, student_id):
    student = Student.objects.get(pk=student_id)
    
    project_ex = Student_experience.objects.filter(student=student)
    
    
    context = {
        'student': student,
        
        'project_ex':project_ex
    }
    return render(request, 'manage_app/view_pro_ex_pro.html',context=context)



@login_required
def viewaddCourse(request):
    course = Course.objects.all()

    return render(request, 'manage_app/add_course.html',context={'course':course})
@login_required
@permission_required('auth.view_user')
def addpro_ex(request, student_id):
    
    
    msg_p = ''
    student = Student.objects.get(pk=student_id)

    if request.method == 'POST':
        experience = Project_experience.objects.create(
            
            name=request.POST.get('name'),
            Project_topic=request.POST.get('Project_topic'),
            desc=request.POST.get('desc'),
            
        )
        
        
        stu_proex =Student_experience.objects.create(
            experience=experience,
            student=student,
        ) 
        
        stu_proex.save()
        experience.save()
       
        msg_p = 'Successfully create new  project experience'
        print (experience.student)
        print(experience)
        print(stu_proex.student)
  
    else:  
        experience = Project_experience.objects.none() 
        stu_proex = Student_experience.objects.none() 
    context = {
       
       'experience':experience,
        'msg_p': msg_p,
        'student': student,
        'stu_proex':stu_proex
    }

    return render(request, 'manage_app/add_project_ex.html', context=context)




@login_required   
@permission_required('manage_app.add_course')
def addCourse(request):
    msg = ''
    
    if request.method == 'POST':
        course = Course.objects.create(
            
            name=request.POST.get('name'),
            desc=request.POST.get('desc'),

           
        )
        course.save()
        teacher=Teacher.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            contect=request.POST.get('contect'),
            
        )
        teacher.save()
        tea_course=Taught_By.objects.create(
            course=course,
            teacher=teacher,

        )
        tea_course.save()
        msg = 'Successfully create new name courese'
    else:
        course = Course.objects.none()

    context = {
       
       'course':course,
        'msg': msg,
        'teacher':teacher,
        'tea_course':tea_course

    }

    return render(request, 'manage_app/add_course.html', context=context)
@login_required   

def viewCourse(request):
    course = Course.objects.all()

    return render(request, 'manage_app/view_course.html',context={'course':course})
@login_required
@permission_required('manage_app.delete_course')
def deleteCourse(request,course_id):
    """
        ลบข้อมูล course โดยลบข้อมูลที่มี id = course_id
    """
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect(to='view_course')

# ส่วนของหน้า Project
@login_required
def selectProject(request, course_id):
    course = Course.objects.get(pk=course_id)
    projectall = Course_Assign.objects.filter(course=course)
    return render(request, 'manage_app/project.html',context={
        'projectall': projectall,
        'course' : course,}
    )

@login_required   
@permission_required('manage_app.add_project')
def addProject(request, course_id):
    msg_p = ''
    course = Course.objects.get(pk=course_id)

    if request.method == 'POST':
        project = Project.objects.create(
            
            name=request.POST.get('name'),
            desc=request.POST.get('desc'),
            min_member=request.POST.get('min_member'),
            mex_member=request.POST.get('mex_member'),
        )
        project.save()
        course_a = Course_Assign.objects.create(
            project=project ,
            course=course
        )
        course_a.save()
        msg_p = 'Successfully create new name project'
        return redirect('find_project_project', course_id=course_id)
    else:
        project = Project.objects.none()

    context = {
       
       'project':project,
        'msg_p': msg_p,
        'course': course
    }

    return render(request, 'manage_app/add_project.html', context=context)
@login_required
def deleteProject(request, course_id, project_id):
    course = Course.objects.get(pk=course_id)
    project = Project.objects.get(id=project_id)
    project.delete()
    return redirect('find_project_project', course_id=course_id)



@login_required
@permission_required('manage_app.view_group')
def viewGroup(request, course_id, project_id):
    search = request.GET.get('search', '')
    groups = Group.objects.filter(project_id__id = project_id).filter(name__icontains = search).annotate(num_member=Count('student_join__student'))
    project = Project.objects.get(pk = project_id)
    course = Course.objects.get(pk = course_id)

    return render(request, 'manage_app/group.html',context={'groups':groups, 
                                                                'project' : project,
                                                                'course' : course,
                                                                'search': search})
@login_required
@permission_required('manage_app.add_group')
def addGroup(request, course_id, project_id):
    error=""
    group = Group.objects.none()
    try:
        project = Project.objects.get(pk = project_id)
        course = Course.objects.get(pk = course_id)
        Student_Join.objects.get(
            group__project_id=project_id,
            student=Student.objects.get(user=request.user),
        )
        error = "You're already have group in this project"
    except Student.DoesNotExist:
        return redirect('view_group', course_id, project_id)
    except Project.DoesNotExist:
        return redirect('view_group', course_id, project_id)
    except Course.DoesNotExist:
        return redirect('view_group', course_id, project_id)
    except Student_Join.DoesNotExist:
        if request.method == 'POST':
        
            group = Group.objects.create(    
                name=request.POST.get('name'),
                project_topic=request.POST.get('desc'),
                project_id = project,
            )
            group.save()
            join = Student_Join.objects.create(    
                group=group,
                student=Student.objects.get(user=request.user),
            )
            join.save()
            create = Student_Create.objects.create(    
                group=group,
                student=Student.objects.get(user=request.user),
            )
            create.save()
            return redirect('view_group', course_id=course_id, project_id= project_id)

    context = {
       'group':group,
       'project' : project,
        'course' : course,
        'error': error,
    }
    return render(request, 'manage_app/add_group.html', context=context)                                                    


@login_required 
@permission_required('manage_app.delete_group')
def deleteGroup(request, course_id, project_id, group_id):
    
    try:
        creater = Student_Create.objects.get(group_id = group_id)
        if request.user.id == creater.student.user.id:
            group = Group.objects.get(pk = group_id )  
            group.delete()
        else:
            return redirect('view_group', course_id, project_id)
    except Group.DoesNotExist:
        return redirect('view_group', course_id, project_id)
    except Student_Create.DoesNotExist:
        return redirect('view_group', course_id, project_id)
    
    return redirect('view_group', course_id, project_id)

@login_required   
@permission_required('manage_app.view_student_join')
def viewMember(request, course_id, project_id, group_id):

    try:
        course = Course.objects.get(pk = course_id)
        group = Group.objects.get(pk = group_id)
        creater = Student_Create.objects.get(group_id = group_id)
        project = Project.objects.get(pk = project_id)
    except Course.DoesNotExist:
        return redirect('view_group', course_id, project_id)
    except Group.DoesNotExist:
        return redirect('view_group', course_id, project_id)
    except Student_Create.DoesNotExist:
        return redirect('view_group', course_id, project_id)
    except Project.DoesNotExist:
        return redirect('view_group', course_id, project_id)

    return render(request, 'manage_app/member.html',context={'group':group, 
                                                                'project' : project,
                                                                'course' : course,
                                                                'creater': creater,
                                                                })


@api_view(['GET',"POST"])
def loadMember(request, group_id):
    if request.method == 'GET':
        items = Student_Join.objects.filter(group=group_id)
        serializer = Student_JoinSerializer(items, many=True)
        return JsonResponse(serializer.data, status=200, safe = False)

    elif request.method == 'POST':
        error = ''
        inp = request.data
        data = {}
        members = Student_Join.objects.filter(group_id = group_id)
        try:
            student = Student.objects.get(user_id__username = inp['user'])
            project = Project.objects.get(pk = inp['project'])
            try:
                already = Student_Join.objects.get(
                    student_id = student.id,
                    group_id__project_id = inp['project']
                )
                error = 'This student is already has group in this project'
                return JsonResponse({'status':'false','error':error}, status=500)
            except Student_Join.DoesNotExist:
                if members.count() >= project.mex_member:
                    error = 'This group is full'
                    return JsonResponse({'status':'false','error':error}, status=500)
                else:
                    data['group'] = inp['group']
                    data['student'] = student.id
                    serializer = Student_JoinSerializer(data = data)
                    if serializer.is_valid():
                        serializer.save()
                    return JsonResponse(serializer.data, status=201, safe = False)
                return JsonResponse(serializer.errors, status=400, safe = False)
        except Student.DoesNotExist:
            error = 'Not found this username'
            return JsonResponse({'status':'false','error':error}, status=500)
        except Project.DoesNotExist:
            error = 'Not found this project'
            return JsonResponse({'status':'false','error':error}, status=500)

        
        
            
        

@login_required
@permission_required('manage_app.delete_student_join') 
def deleteMember(request, group_id, user_id):
    message = ''
    try:
        creater = Student_Create.objects.get(group_id = group_id)
        if request.user.id == creater.student.user.id:
            join = Student_Join.objects.get(
                student_id = user_id,
                group_id = group_id,
            )  
            join.delete()
        else:
            message = "You don't have permission"
            return JsonResponse({'status':'false','error':message}, status=500)
    except Student_Join.DoesNotExist:
        message = "Student not found"
        return JsonResponse({'status':'false','error':message}, status=500)
    except Student_Create.DoesNotExist:
        message = "Group not found"
        return JsonResponse({'status':'false','error':message}, status=500)
    return HttpResponse(status=200)
