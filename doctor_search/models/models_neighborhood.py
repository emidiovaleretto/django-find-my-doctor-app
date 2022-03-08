from doctor_search.models import *


class Neighborhood(models.Model):
    district = models.ForeignKey(District, null=True, related_name='district', on_delete=models.SET_NULL)
    name = models.CharField(null=False, max_length=30)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.district.name}'
