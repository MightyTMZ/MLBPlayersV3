from django.contrib import admin
from .models import Team


class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'league', 'division', 'img_url', 'identification'
    )


admin.site.register(Team, TeamAdmin)