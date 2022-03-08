from doctor_search.models import *


class County(models.Model):
    name = models.CharField(null=False, max_length=20)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
