from django import forms
from django.forms import ModelForm
from .models import Comment, Home, Element, Contact

class HomeForm(ModelForm):
    class Meta:
        model = Home
        fields = ('name','phone_number','email')
        labels = {
            'name': '',
            'phone_number': '',
            'email': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','id':'name', 'name':'name', 'placeholder':'Ism', 'onfocus':'this.placeholder=""','onblur':'this.placeholder="Ism"'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control','id':'subject', 'name':'subject', 'placeholder':'Telefon Raqam', 'onfocus':'this.placeholder=""','onblur':'this.placeholder="Telefon Raqam"'}),
            'email': forms.EmailInput(attrs={'class':'form-control','id':'email', 'name':'email', 'placeholder':'Elektron Pochta', 'onfocus':'this.placeholder=""','onblur':'this.placeholder="Elektron Pochta"'}),
        }

class ElementForm(ModelForm):
    class Meta:
        model = Element
        fields = ('name','sourname','email','address','phone_number','message')
        labels = {
            'name': '',
            'sourname':'',
            'email':'',
            'address':'',
            'phone_number':'',
            'message':'',
            }
        widgets = {
            'name': forms.TextInput(attrs={'type':'text', 'name':'first_name', 'placeholder':'Ism', 'onfocus':'this.placeholder = ""', 'onblur':'this.placeholder = "Ism"', 'required class':'single-input'}),
            'sourname': forms.TextInput(attrs={'type':'text', 'name':'last_name', 'placeholder':'Familiya', 'onfocus':'this.placeholder = ""', 'onblur':'this.placeholder = "Familiya"', 'required class':'single-input'}),
            'email':forms.TextInput(attrs={'type':'text', 'name':'email', 'placeholder':'Elektron Pochta', 'onfocus':'this.placeholder = ""', 'onblur':'this.placeholder = "Elektron Pochta"', 'required class':'single-input'}),
            'address':forms.TextInput(attrs={'type':'text', 'name':'address', 'placeholder':'Manzil', 'onfocus':'this.placeholder = ""', 'onblur':'this.placeholder = "Manzil"', 'required class':'single-input'}),
            'phone_number':forms.TextInput(attrs={'type':'text', 'name':'phone', 'placeholder':'Telefon Raqam', 'onfocus':'this.placeholder = ""', 'onblur':'this.placeholder = "Telefon Raqam"', 'required class':'single-input'}),
            'message':forms.TextInput(attrs={'name':'message', 'placeholder':'Xabar (shart emas)', 'onfocus':'this.placeholder = ""', 'onblur':'this.placeholder = "Xabar (shart emas)"', 'required class':'single-textarea'}),
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','comment')
        labels = {
            'name':'',
            'email':'',
            'comment':'',
        }
        widgets = {
            'name': forms.TextInput(attrs={'type':'text', 'class':'form-control', 'id':'name', 'placeholder':'Ism', 'onfocus':'this.placeholder = ', 'onblur':'this.placeholder = "Ism"'}),
            'email': forms.EmailInput(attrs={'type':'email', 'class':'form-control', 'id':'email', 'placeholder':'Elektron Pochta', 'onfocus':'this.placeholder = ', 'onblur':'this.placeholder = "Elektron Pochta"'}),
            'comment': forms.Textarea(attrs={'class':'form-control mb-10', 'rows':'5', 'name':'message', 'placeholder':'Xabar Matni', 'onfocus':'this.placeholder = ', 'onblur':'this.placeholder = "Xabar Matni"', 'required':''})
        }

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('name','email','theme','message')
        labels = {
            'name': '',
            'email': '',
            'theme': '',
            'message':'',
        }
        widgets = {
            'name': forms.TextInput(attrs={'name':'name', 'placeholder':'Ism', 'onfocus':'this.placeholder = ' ,'onblur':'this.placeholder = "Ism"','class':'common-input mb-20 form-control', 'required':'', 'type':'text'}),
            'email': forms.EmailInput(attrs={'name':'email', 'placeholder':'Elektron Pochta', 'pattern':'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{1,63}$','onfocus':'this.placeholder = ', 'onblur':'this.placeholder = "Elektron Pochta"', 'class':'common-input mb-20 form-control','required':'', 'type':'email'}),
            'theme': forms.TextInput(attrs={'name':'subject', 'placeholder':'Mavzu', 'onfocus':'this.placeholder = ""', 'onblur':'this.placeholder = "Mavzu"','class':'common-input mb-20 form-control', 'required':'','type':'text'}),
            'message': forms.Textarea(attrs={'class':'common-textarea form-control', 'name':'message', 'placeholder':'Xabar', 'onfocus':'this.placeholder = "','onblur':'this.placeholder = "Xabar"', 'required':''})
        }