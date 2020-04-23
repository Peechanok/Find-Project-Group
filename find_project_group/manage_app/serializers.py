from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Group, Student_Join, Student



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','id']

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Student
        fields = ['id','major','contect', 'year', 'user']
        read_only_fields = ['id',]

class Student_JoinSerializer(serializers.ModelSerializer):
    student_detail = StudentSerializer(source='student', read_only=True)
    class Meta:
        model = Student_Join
        fields = ['id','group','student','student_detail']
        read_only_fields = ['id', 'student_detail']
