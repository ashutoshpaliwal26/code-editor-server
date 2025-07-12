from django.urls import path
from authentication.views.login_view import LoginView
from authentication.views.register_view import RegisterUser
urlpatterns = [
    path('signup', RegisterUser.as_view(), name='Signup'),
    path('login', LoginView.as_view(), name='Login'),
]