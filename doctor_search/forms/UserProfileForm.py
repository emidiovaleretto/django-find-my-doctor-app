from django.forms import ModelForm
from django import forms
from doctor_search.models.models_profile import Profile


class UserProfileForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.role != 1:
            del self.fields['role']

    class Meta:
        model = Profile
        fields = [
            'user',
            'role',
            'birthday',
            'image',
        ]
        widgets = {
            'user': forms.HiddenInput(),
            'role': forms.Select(attrs={
                'class': 'form-control',
            }),
            'birthday': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'image': forms.FileField(attrs={
                'class': 'form-control'
            })
        }
