from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import *
from django import forms
class StudentForm(forms.ModelForm):
    
    class Meta:
        
        model = Student
        fields ='__all__'
        exclude = ['user']
       
        labels ={
            'year' :'Year',
            'major':'Major',
            'contect' :'Contect',
            'profile_pic':'Profile Image'}
        widgets = {
            'year': forms.TextInput(attrs={
            'class': 'form-control',
            
            }),
            'major': forms.TextInput(attrs={
            'class': 'form-control',
            }),
            'contect': forms.Textarea(attrs={
            'rows': 3,
            
            'class': 'form-control',
            })
         }
        

class UserForm(ModelForm):
   class Meta:
       model = User
       fields = ['username','first_name','last_name']
       labels ={
            'username' :'User ID',
            'first_name' :'First Name',
            'last_name' :'First Name',}

class Project_experienceFrom(ModelForm):
    
    class Meta:
        
        model = Project_experience
        fields ='__all__'
        exclude = ['student']