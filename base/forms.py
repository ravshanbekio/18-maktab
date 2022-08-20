from django import forms
from .models import Contact, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        exclude = ['blog','user']

        labels = {
            'comment':'',
        }

        widgets = {
            'comment':forms.Textarea(attrs={'class':'form-control mb-10', 'rows':'5', 'name':'message', 
            'placeholder':'Xabar Matni', 
            'onfocus':'this.placeholder = ', 'onblur':'this.placeholder = "Xabar Matni"', 'required':''}),
        }

class AuthenticatedUserContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('message',)
        exclude = ['user',]

        labels = {
            'message':'',
        }

        widgets = {
            'message': forms.Textarea(attrs={'class':'common-textarea form-control', 'name':'message', 'placeholder':'Xabar', 'onfocus':'this.placeholder = "','onblur':'this.placeholder = "Xabar"', 'required':''})
        }


class AnonymousUserContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name','email','message')

        labels = {
            'name':'',
            'email':'',
            'message':'',
        }

        widgets = {
            'name': forms.TextInput(attrs={'name':'name', 'placeholder':'Ism', 'onfocus':'this.placeholder = ' ,'onblur':'this.placeholder = "Ism"','class':'common-input mb-20 form-control', 'required':'', 'type':'text'}),
            'email': forms.EmailInput(attrs={'name':'email', 'placeholder':'Elektron Pochta', 'pattern':'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{1,63}$','onfocus':'this.placeholder = ', 'onblur':'this.placeholder = "Elektron Pochta"', 'class':'common-input mb-20 form-control','required':'', 'type':'email'}),
            'message': forms.Textarea(attrs={'class':'common-textarea form-control', 'name':'message', 'placeholder':'Xabar', 'onfocus':'this.placeholder = "','onblur':'this.placeholder = "Xabar"', 'required':''})
        }