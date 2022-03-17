from django.urls import path
from doctor_search.views.HomeViews import home_view

urlpatterns = [
    path('', home_view)
]
