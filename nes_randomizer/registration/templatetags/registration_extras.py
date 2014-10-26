from django import template
from django.contrib.auth.models import User
from nes.models import BeatenGame, OwnedGame

# removes all entries in BeatenGame and Owned game
# for a user then deletes the user
def delete_user(user):
    print 'deleting beaten games for: %s' % user.username
    BeatenGame.objects.filter(user_id=user.id).delete()
    print 'deleting owned games for: %s' % user.username
    OwnedGame.objects.filter(user_id=user.id).delete()
    # User.objects.filter(user_id=user.id).delete()
    