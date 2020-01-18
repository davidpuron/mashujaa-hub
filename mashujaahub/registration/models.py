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
    ('NO', 'None'),
]

class Artisan(models.Model):
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, blank=False, default='NO')
    name = models.CharField(max_length=30, blank=False, default='None')
    phone = models.CharField(max_length=10, blank=False, default='None')

    def __str__(self):
        return self.name
