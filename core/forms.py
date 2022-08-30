from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import PasswordInput, EmailInput, TextInput
from .models import Contacto

class CustomerUserCreation(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = TextInput(attrs={'placeholder': 'Usuario', 'class': 'form-control'})
        self.fields['first_name'].widget = TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control'})
        self.fields['last_name'].widget = TextInput(attrs={'placeholder': 'Apellido', 'class': 'form-control'})
        self.fields['email'].widget = EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'})
        self.fields['password1'].widget = PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control'})
        self.fields['password2'].widget = PasswordInput(attrs={'placeholder': 'Confirme la contraseña', 'class': 'form-control'})
    class Meta:
        model = User
        fields =['username','first_name','last_name','email','password1','password2']

class ContactoForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    asunto = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Contacto
        fields = ['nombre','email','asunto']
