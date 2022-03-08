from doctor_search.models import *


class DayWeek(models.Model):

    ''' This model will return the days 
    of the week when the doctor will attend '''

    name = models.CharField(null=False, max_length=20)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
