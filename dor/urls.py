
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from dor.apps import DorConfig
from dor.views import RegisterView, verify, generate_new_password, ProfileView

app_name = DorConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('verify/<code>/', verify, name='verify_email'),
    path('logout/genpassword/', generate_new_password, name='generate_new_password'),
    path('profile/', ProfileView.as_view(), name='profile'),

]