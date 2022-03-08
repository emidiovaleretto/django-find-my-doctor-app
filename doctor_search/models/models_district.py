from doctor_search.models import *


class District(models.Model):
    county = models.ForeignKey(County, null=True, related_name='county', on_delete=models.SET_NULL)
    name = models.CharField(null=False, max_length=30)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.county.name}'
