
from django.contrib import admin
from OBGG.models import ComT, MatchT, PlayerT, TeamScoreT, TeamT, UserT
from .import models

class xcomt(admin.ModelAdmin):
    list_display = ["xp1","xp2","xp3","xp4","xp5","xp6","xp7","xp8","xp9","xp10"]
admin.site.register(ComT,xcomt)

class xmatcht(admin.ModelAdmin):
    list_display = ["xp1","xp2","xp3","xp4","xp5","xp6"]
admin.site.register(MatchT,xmatcht)

class XplayerT(admin.ModelAdmin):
    list_display = ["xp1","xp2","xp3","xp4","xp5","xp6","xp7","xp13","xp8","xp9","xp10","xp11","xp12"]
admin.site.register(models.PlayerT,XplayerT)

class xtst(admin.ModelAdmin):
    list_display = ["xp1","xp2","xp3","xp4","xp5","xp6","xp7"]
admin.site.register(TeamScoreT,xtst)

class xtt(admin.ModelAdmin):
    list_display = ["xp1","xp2","xp3","xp4","xp5"]
admin.site.register(TeamT,xtt)


class xuser(admin.ModelAdmin):
    list_display = ["xp1","xp2","xp3","xp4","xp5","xp6","xp7","xp8"]
admin.site.register(UserT,xuser)
# Register your models here.
