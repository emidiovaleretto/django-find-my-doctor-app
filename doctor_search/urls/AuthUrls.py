from django.urls import path
from doctor_search.views.AuthViews import login_view

urlpatterns = [
    path('login', login_view, name='login')
]
