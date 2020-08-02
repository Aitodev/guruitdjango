from django.contrib import admin
from .models import Applications


class SubscribeConfig(admin.ModelAdmin):
    fields = ('mail', 'name', 'comment')
    list_display = ('name', 'mail', 'date', 'comment')


admin.site.register(Applications)


