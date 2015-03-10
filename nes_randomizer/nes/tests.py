from django.test import TestCase
from .templatetags import nes_extras as NES
from nes.models import Game
import urllib2

# Create your tests here.

class NesViewsTests(TestCase):
    link = 'http://127.0.0.1:8000/nes/games/'

    def test_game_details_view(self):
        games = Game.objects.all()

        for game in games:
            print game.id

        g_link = ''.join((self.link, '123'))
        b_link = ''.join((self.link, '999'))


        g_url = urllib2.urlopen(g_link)

        self.assertEquals(
            g_url.getcode(),
            200,
            )
        try:
            b_url = urllib2.urlopen(b_link)
            self.assertEquals(
                b_url.getcode(),
                404,
                )

        except urllib2.HTTPError as e:
            self.assertEquals(
                e.getcode(),
                404,
                )
