from django.shortcuts import render, redirect, get_object_or_404
from doctor_search.models import Profile
from django.core.paginator import Paginator
from doctor_search.forms.UserProfileForm import UserProfileForm


def list_profile_view(request, id=None):
    profile = None
    if id is None and request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user)[0]
    elif id is not None:
        profile = Profile.objects.filter(user__id=id)[0]
    elif not request.user.is_authenticated:
        return redirect(to='/')

    favorites = profile.show_favorites()

    if len(favorites) > 0:
        paginator = Paginator(favorites, 8)
        page = request.GET.get('page')
        favorites = paginator.get_page(page)

    ratings = profile.show_ratings()

    if len(ratings) > 0:
        paginator = Paginator(ratings, 8)
        page = request.GET.get('page')
        ratings = paginator.get_page(page)

    context = {
        'profile': profile,
        'favorites': favorites,
        'ratings': ratings
    }

    return render(request, 'profile/profile.html', context=context, status=200)


def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)
    profile_form = UserProfileForm(instance=profile)

    context = {
        'profile_form': profile_form
    }

    return render(request, 'user/profile.html', context=context)
