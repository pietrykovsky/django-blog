from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.views.generic.edit import FormView

from blog.settings import EMAIL_HOST_USER
from .forms import NewsletterSignupForm, ContactForm

# Create your views here.
def add_to_newsletter(request):
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST or None)
        if form.is_valid():
            form.save()
                
    return redirect(reverse('home'))

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')
    
    def form_valid(self, form):
        email_from = form.cleaned_data['email']
        subject = form.cleaned_data['subject']
        message = 'from: ' + email_from + '\n\n' + form.cleaned_data['message']
        
        send_mail(subject, message, EMAIL_HOST_USER, [EMAIL_HOST_USER])
            
        return super().form_valid(form)

def contact_success(request):
    return render(request, 'contact_success.html')