from django.test import TestCase
from .templatetags import nes_extras as NES
from models import Game

# Create your tests here.

class NESMethodTests(TestCase):
    
    def nes_guid_url_builder(self):
        """
        nes_guid_url_builder() should return...
        """
        games = Game.objects.all()
        
        for game in games.
            