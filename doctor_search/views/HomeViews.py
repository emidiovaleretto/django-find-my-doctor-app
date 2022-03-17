from django.http import HttpResponse

def home_view(request):
    return HttpResponse('<h1>Hello, world!</h1>')