from django.urls import path
from doctor_search.views.DoctorViews import list_doctor_view, add_favorite_view, remove_favorite_view, rate_doctor


urlpatterns = [
    path('', list_doctor_view, name='doctors'),
    path('favorite', add_favorite_view, name='doctor-favorite'),
    path('favorite/remove', remove_favorite_view, name='remove-doctor-favorite'),
    path('rating/<doctor_id:int>', rate_doctor(request), name='rating-doctor'),
]
