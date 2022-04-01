from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from doctor_search.models import Profile, Rating
from doctor_search.forms.DoctorForm import DoctorRatingForm
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
            doctors = doctors.filter(
                addresses__neighborhood__district=district)
        elif county is not None:
            doctors = doctors.filter(
                addresses__neighborhood__city__county=county)

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


def add_favorite_view(request):
    page = request.POST.get('page')
    name = request.POST.get('name')
    speciality = request.POST.get('speciality')
    neighborhood = request.POST.get('neighborhood')
    district = request.POST.get('district')
    county = request.POST.get('county')
    id = request.POST.get('id')

    try:
        profile = Profile.objects.filter(user=request.user)[0]
        doctor = Profile.objects.filter(user__id=id)[0]
        profile.favorites.add(doctor.user)
        profile.save()
        msg = 'Doctor successfully added to favorites.'
        _type = 'success'

    except Exception as e:
        print(f'Error: {e}')
        msg = 'Something went wrong while trying to add the doctor to favorites.'
        _type = 'warning'

    if page:
        arguments = f'?page={page}'
    else:
        arguments = '?page=1'

    if name:
        arguments += f'&name={name}'
    if speciality:
        arguments += f'&speciality={speciality}'
    if neighborhood:
        arguments += f'&neighborhood={neighborhood}'
    if district:
        arguments += f'&district={district}'
    if county:
        arguments += f'&county={speciality}'

    arguments += f'&msg={msg}&type={_type}'

    return redirect(to=f'/doctors/{arguments}')


def remove_favorite_view(request):
    page = request.POST.get('page')
    id = request.POST.get('id')

    try:
        profile = Profile.objects.filter(user=request.user)[0]
        doctor = Profile.objects.filter(user__id=id)[0]
        profile.favorites.remove(doctor.user)
        profile.save()
        msg = 'Doctor successfully removed from favorites'
        _type = 'success'
    except Exception as e:
        print(f'Error: {e}')
        msg = 'Something went wrong while trying to remove the doctorfrom favorites.'
        _type = 'warning'

    if page:
        arguments = f'?page={page}'
    else:
        arguments = '?page=1'

    arguments += f'&msg={msg}&type={_type}'

    return redirect(to=f'/profile/{arguments}')

@login_required
def rate_doctor(request, doctor_id=None):
    doctor = Profile.objects.filter(user__id=doctor_id).first()
    rating = Rating.objects.filter(
        user=request.user, user_rated=doctor.user).first()
    message = None
    initial = {
        'user': request.user,
        'user_rated': doctor.user
    }

    if request.method == 'POST':
        rating_form = DoctorRatingForm(
            request.POST, instance=rating, initial=initial)
    else:
        rating_form = DoctorRatingForm(instance=rating, initial=initial)

    if rating_form.is_valid():
        rating_form.save()
        message = {
            'type': 'success',
            'text': 'Thank you! Your rating has been saved successfully.'
        }

    else:
        if request.method == 'POST':
            message = {
                'type': 'danger',
                'text': 'Something went wrong while trying to save your rating.'
            }

    context = {
        'rating_form': rating_form,
        'doctor': doctor,
        'message': message
    }

    return render(request, 'doctors/rating.html', context=context)