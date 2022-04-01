from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from doctor_search.models import Profile
from django.core.paginator import Paginator
from doctor_search.forms.UserProfileForm import UserProfileForm, UserForm


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

@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)

    is_email_unused = True
    message = None

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        user_form = UserForm(instance=request.user)
        verify_email = Profile.objects.filter(
            user__email=request.POST['email']).exclude(user__id=request.user.id).first()
        is_email_unused = verify_email is None
    else:
        profile_form = UserProfileForm(instance=profile)
        user_form = UserForm(instance=request.user)

    if profile_form.is_valid() and user_form.is_valid() and is_email_unused:
        profile_form.save()
        user_form.save()
        message = {
            'type': 'success',
            'text': 'Data successfully updated'
        }
    else:
        if request.method == 'POST':
            if is_email_unused:
                message = {
                    'type': 'danger',
                    'text': 'Invalid data.'
                }
            else:
                message = {
                    'type': 'warning',
                    'text': f"The email address \"{request.POST['email']}\" is already in use."
                }

    context = {
        'profile_form': profile_form,
        'user_form': user_form,
        'message': message
    }

    return render(request, 'user/profile.html', context=context)
