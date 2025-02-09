from django.contrib import admin
from .models import Profile, Poem
# Register your models here.
admin.site.register(Poem)
admin.site.register(Profile)