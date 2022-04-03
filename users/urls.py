from django.urls import path
from .views import UserRegistrationView, UserLoginView, UserLogoutView, UserProfileView, UserEditView, UserPasswordResetView, UserPasswordResetDoneView, UserPasswordResetConfirmView, UserPasswordResetCompleteView, UserPasswordChangeView, UserPasswordChangeDoneView, toggle_user_redactor

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('password_reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', UserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', UserPasswordChangeDoneView.as_view(), name='password_change_done'),
    path('<int:pk>/profile/', UserProfileView.as_view(), name='profile'),
    path('<slug:slug>/profile/', UserProfileView.as_view(), name='profile'),
    path('profile/edit/', UserEditView.as_view(), name='edit'),
    path('<int:pk>/profile/toggle_redactor/', toggle_user_redactor, name='toggle_redactor'),
]