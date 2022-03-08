from doctor_search.models import *

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rode = models.IntegerField(choices=ROLE_CHOICE, default=3)
    birthday = models.DateField(default=None, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)
    token = models.CharField(max_length=255, null=True, blank=True)
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