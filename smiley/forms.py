from django.contrib.auth.models import User
from django import forms
from smiley.models import User

class ImForm(forms.ModelForm):
	class Meta:
		model=User
		fields=['age','gender','impf','username','email']
		widgets={
		"age":forms.NumberInput(attrs={"class":"form-control","placeholder":"update age",}),
		"gender":forms.Select(attrs={"class":"form-control","placeholder":"Select your gender",}),
        "impf":forms.FileInput(attrs={"class":"form-control","placeholder":"select your profile image",}),
        "username":forms.TextInput(attrs={"class":"form-control"}),
		"email":forms.EmailInput(attrs={"class":"form-control","placeholder":"updateemail",}),
		}

