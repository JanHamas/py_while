from django import forms
class StudentRegistration(forms.Form):
 name = forms.CharField()
 email = forms.EmailField(min_length=5, max_length=50,required=False )
 password = forms.CharField(widget=forms.PasswordInput,) 

