from django.urls import path
from .views import add_to_newsletter, ContactView, contact_success

urlpatterns = [
    path('add_to_newsletter/', add_to_newsletter, name='add_to_newsletter'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/success', contact_success, name='contact_success'),
]