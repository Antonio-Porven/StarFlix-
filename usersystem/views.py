from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from shows.models import Show, Movie,Category, Profile

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('home')  # Redirect to the login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')

        else:
            pass
            # Return an 'invalid login' error message.
            messages.success(request, ('Username or Password is incorrect please try again'))
            return redirect('login')

    else:
        return render(request , 'login.html')

def logout_user(request):
    logout(request)
    return redirect ('home')

def say_hello(request):
    show_list = Show.objects.order_by('?')[:1]
    return render(request , 'homepage.html',
    {'show_list': show_list})




