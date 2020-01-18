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
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES, blank=False, default='NO')
    name = models.CharField(max_length=30, blank=False)
