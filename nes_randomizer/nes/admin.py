from django.contrib import admin
from .models import *
# Register your models here.

class GameAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Game Information', {'fields':['title', 'genre', 'rating', 'votes']}),

    ]
    list_display = ('title', 'genre', 'rating', 'votes')
    list_filter = ['title', 'genre', 'rating']
    search_fields = ['title']

class BeatenAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Beaten Information', {'fields':['user', 'game']}),
    ]
    list_display = ('user', 'game')
    list_filter = ('user', 'game')
    
class OwnedAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Owner Information', {'fields':['user', 'game']}),
    ]
    list_display = ('user', 'game')
    list_filter = ('user', 'game')
    
    
admin.site.register(Game,GameAdmin)
admin.site.register(OwnedGame,OwnedAdmin)
admin.site.register(BeatenGame,BeatenAdmin)