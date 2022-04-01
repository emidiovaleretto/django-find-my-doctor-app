from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from doctor_search.forms.AuthForm import LoginForm


def login_view(request):
    login_form = LoginForm
    message = None

    if request.user.is_authenticated:
        redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                redirect('/')
            else:
                message = {
                    'type': 'danger',
                    'text': 'Invalid data.'
                }

    context = {
        'login_form': login_form,
        'message': message,
        'title': 'Login',
        'button_text': 'Sign in',
        'link_text': 'Register',
        'link_href': '/register'
    }

    return render(request, 'auth/auth.html', context=context)