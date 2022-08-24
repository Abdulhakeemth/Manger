from django.contrib import admin
# Register your models here.
from .models import Userwait,Country,State
admin.site.register(Userwait)
admin.site.register(Country)
admin.site.register(State)