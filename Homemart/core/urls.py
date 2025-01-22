from django.urls import path
from django.contrib.auth import views as auth_views

from .forms import LoginForm
from .views import index, contact, signup

app_name='core'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
]
