from django.contrib.auth.forms import UsernameField
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Student(models.Model):
   user_id = models.OneToOneField(User, on_delete=models.CASCADE)
   year = models.IntegerField()
   contect = models.CharField( max_length=50)
   major = models.CharField( max_length=50)

class Admin(models.Model):
   user_id = models.OneToOneField(User, on_delete=models.CASCADE)

class Project_experience(models.Model):
   student = models.ManyToManyField(Student, through='Student_experience')
   name = models.CharField( max_length=50)
   Project_topic = models.CharField( max_length=50)
   desc = models.TextField()

class Student_experience(models.Model):
   experience = models.ForeignKey(Project_experience, on_delete=models.CASCADE)
   student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Project(models.Model):
   name = models.CharField( max_length=50)
   desc = models.TextField()
   min_member = models.IntegerField()
   mex_member = models.IntegerField()



class Group(models.Model):
   name = models.CharField( max_length=50)
   project_topic = models.CharField( max_length=50)
   project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
   create = models.ManyToManyField(Student, through='Student_Create', related_name='created') 
   join = models.ManyToManyField(Student, through='Student_Join', related_name='Join_group') 

class Student_Create(models.Model):
   group = models.ForeignKey(Group, on_delete=models.CASCADE)
   student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Student_Join(models.Model):
   group = models.ForeignKey(Group, on_delete=models.CASCADE)
   student = models.ForeignKey(Student, on_delete=models.CASCADE)
   

class Course(models.Model):
   name = models.CharField(max_length=50)
   desc = models.TextField()
   admin_id = models.ForeignKey(Admin, on_delete=models.DO_NOTHING, null=True)
   student = models.ManyToManyField(Student, through='Student_Enroll')
   project = models.ManyToManyField(Project, through='Course_Assign')
   

class Student_Enroll(models.Model):
   course = models.ForeignKey(Course, on_delete=models.CASCADE)
   student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Course_Assign(models.Model):
   project = models.ForeignKey(Project, on_delete=models.CASCADE)
   course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Teacher(models.Model):
   first_name = models.CharField( max_length=50) 
   last_name = models.CharField( max_length=50)
   contect = models.CharField( max_length=50)
   course = models.ManyToManyField(Course, through='Taught_By')

class Taught_By(models.Model):
   course = models.ForeignKey(Course, on_delete=models.CASCADE)
   teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
