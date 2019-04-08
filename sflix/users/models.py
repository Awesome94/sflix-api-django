from django.db import models
# from Phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

# Create your models here.

class Users(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.TextField()
    email = models.CharField(max_length=100, blank=True, default='')
    # phone = PhoneNumberField()

    def full_name(self):
        return '{} {}'.format(self.frist_name, self.last_name)

    def __str__(self):
        return self.full_name()
