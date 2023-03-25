from django.contrib import admin
from .models import *


class Player(admin.ModelAdmin):
    list_display = 'name'


class Arizona_DiamondbackAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url', 'team_id')


class Atlanta_BraveAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url', 'team_id'
    )


class Baltimore_OrioleAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url', 'team_id'
    )


class Boston_Red_SoxAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class Chicago_White_SoxAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class Chicago_CubAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class Cincinnati_RedAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class Cleveland_GuardianAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class Colorado_RockieAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class Detroit_TigerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class Houston_AstroAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class Kansas_City_RoyalAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class Los_Angeles_AngelAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class Los_Angeles_DodgerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class Miami_MarlinAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class Milwaukee_BrewerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class Minnesota_TwinAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class New_York_YankeeAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class New_York_MetAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class Oakland_AthleticAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class Philadelphia_PhillieAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class Pittsburgh_PirateAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class San_Diego_PadreAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class San_Francisco_GiantAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class Seattle_MarinerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class St_Louis_CardinalAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class Tampa_Bay_RayAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class Texas_RangerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class Toronto_Blue_JayAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


class Washington_NationalAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'team', 'position', 'img_url'
    )


# all the teams don't end in 's' because django admin automatically adds an 's' at the end of each
admin.site.register(Arizona_Diamondback, Arizona_DiamondbackAdmin)
admin.site.register(Atlanta_Brave, Atlanta_BraveAdmin)
admin.site.register(Baltimore_Oriole, Baltimore_OrioleAdmin)
admin.site.register(Boston_Red_Sox, Boston_Red_SoxAdmin)
admin.site.register(Chicago_White_Sox, Chicago_White_SoxAdmin)
admin.site.register(Chicago_Cub, Chicago_CubAdmin)
admin.site.register(Cincinnati_Red, Cincinnati_RedAdmin)
admin.site.register(Cleveland_Guardian, Cleveland_GuardianAdmin)
admin.site.register(Colorado_Rockie, Colorado_RockieAdmin)
admin.site.register(Detroit_Tiger, Detroit_TigerAdmin)
admin.site.register(Houston_Astro, Houston_AstroAdmin)
admin.site.register(Kansas_City_Royal, Kansas_City_RoyalAdmin)
admin.site.register(Los_Angeles_Dodger, Los_Angeles_DodgerAdmin)
admin.site.register(Los_Angeles_Angel, Los_Angeles_AngelAdmin)
admin.site.register(Miami_Marlin, Miami_MarlinAdmin)
admin.site.register(Milwaukee_Brewer, Milwaukee_BrewerAdmin)
admin.site.register(Minnesota_Twin, Minnesota_TwinAdmin)
admin.site.register(New_York_Yankee, New_York_YankeeAdmin)
admin.site.register(New_York_Met, New_York_MetAdmin)
admin.site.register(Oakland_Athletic, Oakland_AthleticAdmin)
admin.site.register(Philadelphia_Phillie, Philadelphia_PhillieAdmin)
admin.site.register(Pittsburgh_Pirate, Pittsburgh_PirateAdmin)
admin.site.register(San_Diego_Padre, San_Diego_PadreAdmin)
admin.site.register(San_Francisco_Giant, San_Francisco_GiantAdmin)
admin.site.register(Seattle_Mariner, Seattle_MarinerAdmin)
admin.site.register(St_Louis_Cardinal, St_Louis_CardinalAdmin)
admin.site.register(Tampa_Bay_Ray, Tampa_Bay_RayAdmin)
admin.site.register(Texas_Ranger, Texas_RangerAdmin)
admin.site.register(Toronto_Blue_Jay, Toronto_Blue_JayAdmin)
admin.site.register(Washington_National, Washington_NationalAdmin)
