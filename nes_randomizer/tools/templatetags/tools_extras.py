from django import template
from django.contrib.auth.models import User
from nes.models import BeatenGame, OwnedGame

# removes all entries in BeatenGame and Owned game
# for a user then deletes the user
def delete_user(user):
    BeatenGame.objects.filter(user_id=user.id).delete()
    OwnedGame.objects.filter(user_id=user.id).delete()
    User.objects.filter(id=user.id).delete()
    