from django.contrib.auth.forms import UsernameField
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Student(models.Model):
   user_id = models.ForeignKey(User, on_delete=models.CASCADE)
   year = models.IntegerField()
   contect = models.CharField( max_length=50)
   major = models.CharField( max_length=50)
   

class Project_experience(models.Model):
    student_id = models.ForeignKey(Student,  on_delete=models.CASCADE)
    name = models.CharField( max_length=50)
    Project_topic = models.CharField( max_length=50)
    desc = models.TextField()
class Project(models.Model):
   name = models.CharField( max_length=50)
   desc = models.TextField()
   min_member = models.IntegerField()
   mex_member = models.IntegerField()

class Group(models.Model):
   name = models.CharField( max_length=50)
   project_topic = models.CharField( max_length=50)
   project_id = models.ForeignKey(Project, on_delete=models.CASCADE)


class Course(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    student_id = models.ManyToManyField(Student) 
    
class Teacher(models.Model):
 first_name = models.CharField( max_length=50) 
 last_name = models.CharField( max_length=50)
 contect = models.CharField( max_length=50)
 course_id = models.ManyToManyField(Course)



    