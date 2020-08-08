from django.contrib import admin
from .models import Applications, Team


class SubscribeConfig(admin.ModelAdmin):
    fields = ('mail', 'name', 'comment')
    list_display = ('name', 'mail', 'date', 'comment')
    admin.site.register(Applications)


class TeamConfig(admin.ModelAdmin):
    fiels = ('name',
             'img',
             'status',
             'phone',
             'instagram',
             'mail')
    list_display = ('name', 'img', 'status')
    admin.site.register(Team)

