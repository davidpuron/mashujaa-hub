from django.contrib import admin
from registration.models import Artisan
from django.contrib.auth.models import Group,User

class ArtisanAdmin(admin.ModelAdmin):
    list_display=('name','type','phone')
    list_filter=('type',)

admin.site.unregister(Group)
admin.site.register(Artisan, ArtisanAdmin)
