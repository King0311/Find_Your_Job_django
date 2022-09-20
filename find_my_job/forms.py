
from .models import *
from django.forms import ModelForm
from django import forms

class hr_profile_form(ModelForm):
    
    class Meta:
        model = hr_profile
        fields = '__all__'
        widgets = {
            'username':forms.TextInput(attrs={
                'class' : 'inputs',
                'placeholder':'Username',
            }),
            'personal_name':forms.TextInput(attrs={
                'class' : 'inputs',
                'placeholder':'Name'

            }),
            'company_name':forms.TextInput(attrs={
                'class' : 'inputs',
                'placeholder':"Company's Name"
                
            }),
            'email':forms.EmailInput(attrs={
                'class' : 'inputs',
                'placeholder':'Email'
                
            }),
            'company_city':forms.TextInput(attrs={
                'class' : 'inputs',
                'placeholder':'City'
                
            }),
            'post':forms.TextInput(attrs={
                'class' : 'inputs',
                'placeholder':'Looking For?',
                'text-transform': 'lowercase'
                
            }),
        }


class seeker_porfile_form(ModelForm):
    
    class Meta:
        model = seeker_profile
        fields = '__all__'
        widgets = {
             'username':forms.TextInput(attrs={
                'class' : 'inputs',
                'placeholder':'Username'

            }),
            'name':forms.TextInput(attrs={
                'class':'inputs',
                'placeholder':'Name'
            }),
            'current_company_name':forms.TextInput(attrs={
                'class':'inputs',
                'placeholder':'Working for?'
            }),
            'email':forms.EmailInput(attrs={
                'class':'inputs',
                'placeholder':'Email'
            }),
            'profession':forms.TextInput(attrs={
                'class':'inputs',
                'placeholder':'Designation',
                'text-transform': 'lowercase'
            }),
        }
