from django.shortcuts import render



def  auth_social_callback(request):
    return render(request, 'blog/auth/auth_social_callback.html')


def auth_social_error(request):
    return render(request, 'blog/auth/auth_social_error.html')