from django import forms
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField
from .models import Account

class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = Account
        fields = ('first_name','last_name','phone_number',
                'email','username','pupil_class','date_birth')

        labels = {
            'first_name':'',
            'last_name':'',
            'phone_number':'',
            'email':'',
            'username':'',
            'pupil_class':'',
            'date_birth':''
        }

        widgets = {
            'first_name':forms.TextInput(attrs={'type':'text','class':'form-control','placeholder':'Ism'}),
            'last_name':forms.TextInput(attrs={'type':'text','class':'form-control','placeholder':'Familiya'}),
            'phone_number':forms.TextInput(attrs={'type':'text','class':'form-control','placeholder':'Telefon raqam'}),
            'email':forms.EmailInput(attrs={'type':'email','class':'form-control','placeholder':'Elektron pochta'}),
            'username':forms.TextInput(attrs={'type':'text','class':'form-control','placeholder':'Username'}),
            'pupil_class':forms.TextInput(attrs={'class':'form-control','placeholder':"O'quvchi Sinfi"}),
            'date_birth':forms.DateInput(attrs={'class':'form-control', 'placeholder':"O'quvchining tug'ulgan sanasi"}),
        }

    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''
        self.fields['password1'].widget.attrs['placeholder'] = 'Parol'
        self.fields['password2'].widget.attrs['placeholder'] = 'Parolni takrorlang'

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        if commit:
            user.save()
        return user

class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Account
        fields = ('first_name','last_name','phone_number',
                'email','username','pupil_class')

        widgets = {
            'first_name':forms.TextInput(attrs={'type':'text','class':'form-control','placeholder':'Ism'}),
            'last_name':forms.TextInput(attrs={'type':'text','class':'form-control','placeholder':'Familiya'}),
            'phone_number':forms.TextInput(attrs={'type':'text','class':'form-control','placeholder':'Telefon raqam'}),
            'email':forms.EmailInput(attrs={'type':'email','class':'form-control','placeholder':'Elektron pochta'}),
            'username':forms.TextInput(attrs={'type':'text','class':'form-control','placeholder':'Username'}),
            'pupil_class':forms.TextInput(attrs={'class':'form-control','placeholder':"O'quvchi Sinfi"}),
            'date_birth':forms.DateInput(attrs={'class':'form-control'}),
        }
