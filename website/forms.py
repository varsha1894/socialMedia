from django import forms

from .models import Register

class RegisterForm(forms.ModelForm):
	 class Meta:
	 	model = Register
	 	fields = ['name','email','password']

	 def clean_email(self):
	 	email= self.cleaned_data.get1('email')
	 	return email

	 def clean_name(self):
	 	name=self.cleaned_data.get('name')
	 	return name 
	 	
	 def clean_password(self):
	    password=self.cleaned_data.get('password')
	    return password	
	 
    
