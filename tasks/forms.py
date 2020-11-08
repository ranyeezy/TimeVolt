from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['title', 'due', 'complete', 'notes']

class CreateUserForm(UserCreationForm):
	class Meta:
		model=User
		fields = ['username','email','password1','password2']
