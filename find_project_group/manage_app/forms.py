from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Student,User

class StudentForm(ModelForm):
    
    class Meta:
        
        model = Student
        fields =['year','major','contect']
        labels ={
           'year' :'Year','major' :'Major','contact' :'Contact',
        }
class UserForm(ModelForm):
   class Meta:
       model = User
       fields = ['username','password']
       labels ={
            'username' :'User ID',
            'password' :'Password',}