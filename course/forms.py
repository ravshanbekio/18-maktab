from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('message',)
        exclude = ['course','user']

        labels = {
            'message':'',
        }

        widgets = {
            'messages':forms.Textarea(attrs={'name':"feedback", 'class':"form-control", 'cols':"10", 'rows':"10"}),
        }