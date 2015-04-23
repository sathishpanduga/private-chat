from django.contrib import admin

from private_chat import models

admin.site.register(models.Message)
admin.site.register(models.ContactRequest)
admin.site.register(models.Contact)
