from django.contrib import admin
from django.urls import path
from registration import views

admin.site.site_header = "Mashujaa Hub Admin"
admin.site.site_title = "Mashujaa Hub Admin"
admin.site.index_title = "Mashujaa Hub Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
]
