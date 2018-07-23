from django.shortcuts import render
from .templates.CarSalon_App.auth.registerForm import RegisterForm 
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


def application_index(request):
    return render(request,'../templates/CarSalon_App/index.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)

    else:
        form = RegisterForm()
    return render(request, 'CarSalon_App/auth/register.html', {'form': form})       

def view_all_users(request):
   
    users = User.objects.values('first_name','last_name','username','email','is_superuser')

    context = {'users': users}

    return render (request,'CarSalon_App/user/index.html',context)