from django.urls import path
from doctor_search.views.ProfileViews import list_profile_view


urlpatterns = [
    path('', list_profile_view, name='profiles'),
    path('<int:id>/', list_profile_view, name='profile')
]
