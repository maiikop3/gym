from django import forms

class ContactForm(forms.Form):
	Email 	= forms.EmailField(widget=forms.TextInput,help_text='A valid email address, please.')
	Titulo 	= forms.CharField(widget=forms.TextInput())
	Texto	= forms.CharField(widget=forms.Textarea())

class LoginForm(forms.Form):
	username	= forms.CharField(widget=forms.TextInput())
	password 	= forms.CharField(widget=forms.PasswordInput(render_value=False))