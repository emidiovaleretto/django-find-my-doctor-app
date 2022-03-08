from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ROLE_CHOICE = (
    (1, 'Admin'),
    (2, 'Doctor'),
    (3, 'Patient'),
)

from .models_rating import Rating
from .models_day_week import DayWeek
from .models_county import County
from .models_district import District
from .models_neighborhood import Neighborhood
from .models_address import Address
from .models_speciality import Speciality
from .models_profile import Profile