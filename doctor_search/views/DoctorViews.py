from django.http import HttpResponse
from doctor_search.models import Profile
from django.db.models import Q


def list_doctor_view(request):
    name = request.GET.get('name')
    speciality = request.GET.get('speciality')
    neighborhood = request.GET.get('neighborhood')
    district = request.GET.get('district')
    county = request.GET.get('county')

    doctors = Profile.objects.filter(role=3).all()

    if name is not None and name != '':
        doctors = doctors.filter(
            Q(user__first_name__contains=name) |
            Q(user__username__contains=name)
        )
    if speciality is not None:
        doctors = doctors.filter(specialities__id=speciality)

    if neighborhood is not None:
        doctors = doctors.filter(addresses__neighborhood=neighborhood)
    else:
        if district is not None:
            doctors = doctors.filter(
                addresses__neighborhood__district=district)
        elif county is not None:
            doctors = doctors.filter(
                addresses__neighborhood__district__county=county)

    print(doctors.all())

    return HttpResponse('Listing one or more doctors.')
