from doctor_search.models import *
from django.db.models import Sum, Count
from .models_rating import Rating


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE_CHOICE, default=3)
    birthday = models.DateField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    favorites = models.ManyToManyField(User, blank=True, related_name='favorites')
    specialities = models.ManyToManyField(Speciality, blank=True, related_name='specialities')
    addresses = models.ManyToManyField(Address, blank=True, related_name='addresses')

    def __str__(self):
        return f'{self.user.username}'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            if created:
                Profile.objects.create(user=instance)
        except:
            pass

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except:
            pass

    def show_scoring_average(self):
        try:
            ratings = Rating.objects.filter(user_rated=self.user).aggregate(Sum('value'), Count('user'))
            if ratings['user__count'] > 0:
                scoring_average = round(ratings['value__sum'] / ratings['user__count'], 2)
                return scoring_average
            return 'No reviews'
        except:
            return 'No reviews'