from django import forms

from .models import NewsletterSignup


class NewsletterSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Type your email adress',
    'type': 'email',
    'id': 'email',
    'name': 'email'}), 
    label='')
    class Meta:
        model = NewsletterSignup
        fields = ['email']

class ContactForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Type your email adress'}), label='From')
    subject = forms.CharField(max_length=50, required=True)
    message = forms.CharField(max_length=500, required=True, widget=forms.Textarea)
