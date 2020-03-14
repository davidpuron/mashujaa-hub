# Generated by Django 2.1.11 on 2020-01-18 07:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artisan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('BE', 'Beautician'), ('CA', 'Carpenter'), ('EL', 'Electrician'), ('HO', 'House Keeper'), ('ME', 'Mechanic'), ('MA', 'Mason'), ('PA', 'Painter'), ('PL', 'Plumber'), ('TA', 'Tailor'), ('WE', 'Welder'), ('GE', 'Generation and Solar'), ('NO', 'None')], default='NO', max_length=2)),
                ('name', models.CharField(max_length=30)),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]