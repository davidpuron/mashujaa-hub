from django.contrib import admin
from registration.models import Artisan

class ArtisanAdmin(admin.ModelAdmin):
    list_display=('name','type','phone')
    list_filter=('type',)

admin.site.register(Artisan, ArtisanAdmin)
