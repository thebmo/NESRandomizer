from django.test import TestCase
from django.contrib.auth.models import User
# from nes.models import BeatenGame, OwnedGame


# Create your tests here.

class RegistrationTests(TestCase):

    def User_Creation_Test(self):
        """
        this tests to verify a user was created successfully
        and that his game data was saved correctly
        """
        username = 'sir_bmo_testington'
        password = 'test123456789'
        email = 'fake_bmo_tester@fake.com'
        
        #creates the user
        user = User.objects.create_user(username, email, password)

        assert User.objects.get(pk=1) == user
        
    # def found_games(games):
        # if games:
            # return True
        # else:
            # return False
        
    # def Beaten_Game_Add_Test(self):
        # for i in range(1, 4):
            # game = BeatenGame(game_id=i, user_id=1)
            # game.save()
        # games = BeatenGame.objects.filter(user_id=1)
        # assert found_games(games) == True
        
        