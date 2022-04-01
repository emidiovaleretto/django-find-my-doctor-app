from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from doctor_search.forms.AuthForm import LoginForm, RegisterForm


def login_view(request):
    login_form = LoginForm()
    message = None

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                _next = request.GET.get('next')
                
                if _next is not None:
                    return redirect(_next)
                else:
                    return redirect('/')
            else:
                message = {
                    'type': 'danger',
                    'text': 'Invalid data.'
                }

    context = {
        'auth_form': login_form,
        'message': message,
        'title': 'Login',
        'button_text': 'Sign in',
        'link_text': 'Register',
        'link_href': '/register'
    }

    return render(request, 'auth/auth.html', context=context)


def register_view(request):
    register_form = RegisterForm()
    message = None

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            verify_first_name = User.objects.filter(
                first_name=first_name).first()
            verify_email = User.objects.filter(email=email).first()

            if verify_first_name is not None:
                message = {
                    'type': 'danger',
                    'text': 'User Name already exists. Please try with another one.'
                }
            elif verify_email is not None:
                message = {
                    'type': 'danger',
                    'text': f"The email \"{request.POST['email']}\" already exists. Please try with another one."
                }

            else:
                user = User.objects.create_user(first_name, last_name, email, password)

                if user is not None:
                    message = {
                    'type': 'success',
                    'text': 'You have successfully registered!'
                    }
                else:
                    message = {
                    'type': 'danger',
                    'text': 'Something went wrong. User Registration failed.'
                    }

    context = {
        'auth_form': register_form,
        'message': message,
        'title': 'Sign up',
        'button_text': 'Sign in',
        'link_text': 'Login',
        'link_href': '/login'
    }

    return render(request, 'auth/auth.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('/')