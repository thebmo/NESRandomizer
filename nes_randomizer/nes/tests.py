from django.test import TestCase
from .templatetags import nes_extras as NES
from nes.models import Game
import urllib2
from random import random

# Create your tests here.

class NesExtrasFunctions(TestCase):
    games = Game.objects.all()
    
        
    def nes_guide_url_builder(game):
        """
        nes_guid_url_builder() should return false if all URLs do not
        404
        """
        try:
            NES.fetch_game_html(game)
            return True
        
        except:
            pass
            print "Failed: %s" % game.title
            return False

            
    for game in games:
        assert nes_guide_url_builder(game) == True