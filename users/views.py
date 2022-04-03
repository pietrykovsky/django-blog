from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import User
from .forms import UserRegistrationForm, UserEditForm
from posts.decorators import user_is_redactor

# Create your views here.
class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')
    redirect_authenticated_user = True

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home') 

class UserLogoutView(LoginRequiredMixin ,LogoutView):
    next_page = 'login'

class UserPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset.html'
    success_url = reverse_lazy('password_reset_done')

class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'

class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'

class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'users/password_reset_complete.html'

class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'users/password_change.html'

class UserPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'users/password_change_done.html'

class UserProfileView(DetailView):
    queryset = User.objects.all()
    query_pk_and_slug = True
    slug_field = 'username'
    context_object_name = 'profile'
    template_name = 'users/profile.html'

class UserEditView(LoginRequiredMixin, UpdateView):
    form_class = UserEditForm
    queryset = User.objects.all()
    template_name = 'users/edit.html'


    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'slug': self.object.username})

    def get_object(self, *args, **kwargs):
        return self.request.user

@user_is_redactor
def toggle_user_redactor(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        if user.is_redactor:
            user.is_redactor = False
            user.save()
        else:
            user.is_redactor = True
            user.save()
    return redirect(reverse('profile', kwargs={'pk': user.pk}))