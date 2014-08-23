from django.contrib import admin
from .models import Game
# Register your models here.

class GameAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Game Information', {'fields':['title', 'genre', 'rating', 'votes']}),

    ]
    list_display = ('title', 'genre', 'rating', 'votes')
    list_filter = ['title', 'genre', 'rating']
    search_fields = ['title']


admin.site.register(Game,GameAdmin)