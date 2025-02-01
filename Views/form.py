from django import forms
from .models import Formulation

class CreateFormulation(forms.ModelForm):
    email = forms.EmailField(label="Email address", 
                             widget=forms.EmailInput(attrs={
        'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 sm:text-sm/6'
    }))  
    
    password = forms.CharField(label="Password", 
                               widget=forms.PasswordInput(attrs={
        'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 placeholder:text-gray-400 focus:outline sm:text-sm/6'
    }))


    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        
        # Here you can authenticate the user or perform additional checks
        return cleaned_data