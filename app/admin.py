from django.contrib import admin
from .models import Note, TelegramPhoto, Profile

admin.site.register(Profile)
admin.site.register(TelegramPhoto)
admin.site.register(Note)
