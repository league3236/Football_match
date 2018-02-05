from django import forms
from django.contrib.auth.models import User
from .models import *

class UserForm(forms.ModelForm):
	class Meta:
		model = Team
		'''
		fields = ('t_call','t_pwd','t_name', 't_leader', 't_place', 't_time', 't_power',)
		'''
		fields = ('t_call','t_pwd',)

class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password',)

