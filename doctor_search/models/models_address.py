from doctor_search.models import *


class Address(models.Model):
    neighborhood = models.ForeignKey(Neighborhood, null=True, related_name='neighborhood', on_delete=models.SET_NULL)
    name = models.CharField(null=False, max_length=30)
    address = models.CharField(null=False, max_length=255)
    latitute = models.DecimalField(max_digits=9, decimal_places=7)
    longitude = models.DecimalField(max_digits=9, decimal_places=7)
    openinig_time = models.TimeField()
    closing_time = models.TimeField()
    days_week = models.ManyToManyField(DayWeek, blank=True, related_name='days_week')
    phone = models.CharField(null=True, blank=True, max_length=50)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
