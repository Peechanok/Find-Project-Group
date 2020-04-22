from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import *

class StudentForm(ModelForm):
    
    class Meta:
        
        model = Student
        fields =['profile_pic']
        exclude = ['user']
       

class UserForm(ModelForm):
   class Meta:
       model = User
       fields = ['username','password']
       labels ={
            'username' :'User ID',
            'password' :'Password',}

class Project_experienceFrom(ModelForm):
    
    class Meta:
        
        model = Project_experience
        fields ='__all__'
        exclude = ['student']