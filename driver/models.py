from django.db import models
class Driver(models.Model):
    first_name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)

    def __str__(self):
        return self.first_name
