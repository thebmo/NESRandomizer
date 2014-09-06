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

class OwnedAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Owner Information', {'fields':['user', 'game', 'beaten']}),
    ]
    list_display = ('user', 'game', 'beaten')
    list_filter = ('user', 'game', 'beaten')
    
    
admin.site.register(Game,GameAdmin)
admin.site.register(OwnedGame,OwnedAdmin)