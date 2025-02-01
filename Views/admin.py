from django.contrib import admin
# Register your models here.
from .models import NavItem, Formulation
admin.site.register(NavItem)
admin.site.register(Formulation)