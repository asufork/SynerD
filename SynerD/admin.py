from django.contrib import admin

# Register your models here.
from .models import Service, Subscriber, Organization

admin.site.register(Service)
admin.site.register(Subscriber)
admin.site.register(Organization)