from django.db import models
from django.contrib.auth.models import User

TYPE_CHOICES = [
    ('BE', 'Beautician'),
    ('CA', 'Carpenter'),
    ('EL', 'Electrician'),
    ('HO', 'House Keeper'),
    ('ME', 'Mechanic'),
    ('MA', 'Mason'),
    ('PA', 'Painter'),
    ('PL', 'Plumber'),
    ('TA', 'Tailor'),
    ('WE', 'Welder'),
    ('GE', 'Generation and Solar'),
    ('OT', 'Other (Please specify)'),
    ('NO', 'None'),
]

class Artisan(models.Model):
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, blank=False, default='NO')
    other_type = models.CharField(max_length=30, blank=False, default='')
    name = models.CharField(max_length=30, blank=False, default='None')
    phone = models.CharField(max_length=10, blank=False, default='None')
    telegramChatId = models.IntegerField(blank=True, default=-1)
    years_of_experience = models.IntegerField(blank=True, default=0)
    contract_signed = models.BooleanField(blank=True, default=False)


    def __str__(self):
        return self.name
