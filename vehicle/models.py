from django.db import models
class Vehicle(models.Model):
    make = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, editable=False, null=False, blank=False)
    plate_number = models.CharField(max_length=250)
    driver_id = models.OneToOneField('driver.Driver', related_name='vehicles', on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.plate_number