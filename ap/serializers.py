import imp
from pyexpat import model
from attr import field
from rest_framework import serializers
from . models import Employee

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee;
        fields='__all__'