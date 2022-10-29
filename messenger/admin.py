from django.contrib import admin

# Register your models here.
from messenger.models import Message

admin.site.register(Message)