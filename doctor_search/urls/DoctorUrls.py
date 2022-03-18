from django.urls import path
from doctor_search.views.DoctorViews import list_doctor_view


urlpatterns = [
    path('', list_doctor_view, name='doctors')
]
