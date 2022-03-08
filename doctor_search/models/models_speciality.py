from doctor_search.models import *


class Speciality(models.Model):

    ''' This model will return the doctor speciality '''

    name = models.CharField(null=False, max_length=100)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
