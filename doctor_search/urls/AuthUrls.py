from django.urls import path
from doctor_search.views.AuthViews import login_view, register_view

urlpatterns = [
    path('login', login_view, name='login'),
    path('register', register_view, name='register'),
]
