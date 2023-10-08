from django.urls import path
from .views import  auth_social_callback,auth_social_error  

app_name= "authentication"

urlpatterns =[
    path('callback', auth_social_callback,name="auth_social_callback"),
    path('auth_social_error', auth_social_error, name="auth_social_error")
]