from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from doctor_search.models.models_profile import Profile
from doctor_search.models.models_rating import Rating
from django.db.models import Q
from django.core.paginator import Paginator


def list_doctor_view(request):
    name = request.GET.get("name")
    speciality = request.GET.get("speciality")
    neighborhood = request.GET.get("neighborhood")
    district = request.GET.get("district")
    county = request.GET.get("county")

    doctors = Profile.objects.filter(role=2)
    if name is not None and name != '':
        doctors = doctors.filter(user__first_name__contains=name)
    if speciality is not None:
        doctors = doctors.filter(specialties__id=speciality)

    if neighborhood is not None:
        doctors = doctors.filter(addresses__neighborhood=neighborhood)
    else:
        if district is not None:
            doctors = doctors.filter(addresses__neighborhood__district=district)
        elif county is not None:
            doctors = doctors.filter(addresses__neighborhood__city__county=county)

    if len(doctors) > 0:
        paginator = Paginator(doctors, 8)
        page = request.GET.get('page')
        doctors = paginator.get_page(page)

    get_copy = request.GET.copy()
    parameters = get_copy.pop('page', True) and get_copy.urlencode()

    context = {
        'doctors': doctors,
        'parameters': parameters
    }

    return render(request, template_name='doctors/doctors.html', context=context, status=200)
