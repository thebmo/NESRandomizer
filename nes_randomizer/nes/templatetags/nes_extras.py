import os, urllib2
import gdata.youtube
import gdata.youtube.service
import re
from django import template
from nes.models import *
from amazon.api import AmazonAPI
from bs4 import BeautifulSoup


register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


# returns a list of youtube objects in a list
def fetch_game_videos(game):
    v_keys = []
    # opens the ytb service
    yt_service = gdata.youtube.service.YouTubeService()

    # authorize - you need to sign up for your own access key, or be rate-limited
    yt_service.developer_key = os.environ['yt_dev']
    yt_service.client_id = os.environ['yt_client']


    query = gdata.youtube.service.YouTubeVideoQuery()

    query.vq = 'NES ' + game.title
    query.max_results = 3
    query.orderby = 'relevance'
    query.racy = 'include'

    feed = yt_service.YouTubeQuery(query)
    for entry in feed.entry:
        v_keys.append(entry.id.text.replace('http://gdata.youtube.com/feeds/videos/', ''))
    
    return v_keys


# returns the html from nesguide.com
def fetch_game_html(game):
    title = game.title
    print title
    
    # possessive games and ', the' games
    if re.search('\'s$', title, flags=re.IGNORECASE) or re.search(', \w*$', title, flags=re.IGNORECASE):
        title = title.split(', ')
        title = ' '.join((title[1], title[0]))
    
    # if re.search(', the .*', title, flags=re.IGNORECASE):
    if re.search(', the', title, flags=re.IGNORECASE):

        if ':' in title:
            temp1 = title.split(':')
            temp2 = temp1[0].split(', ')
            title = temp2[1] + '-' + temp2[0] + temp1[1]
        else:
            title = title.split(',')
            title = ' '.join((title[1], title[0])).strip(' ')


    title = title.replace(':','').replace('IV', '4').replace('III','3').replace('II','2').replace('\'','').replace('\&','and').replace(' / ', '-').lower()
    
    # for stupid roman numeral V
    title = re.sub('\sv$', ' 5', title)
    title = re.sub('\sv?\s', ' 5 ', title)
    
    # corner cases
    # top player tennis
    if 'top player' in title:
        title = 'evert-and-lendl-top-players-tennis'
    # iron sword
    elif title == 'wizards and warriors 2 ironsword':
        title = 'ironsword-wizards-and-warriors-2'
    # wizardry 2
    elif title == 'wizardry knight of diamonds':
        title = 'wizardry-2-knight-of-diamonds'

    # tmnt games
    elif 'tmnt' in title:
        title = title.replace('tmnt', 'teenage mutant ninja turtles')
        # tmnt III
        if '3' in title:
            title = title.replace('the ', '')

    # terminator 2 typo
    elif 'terminator' in title:
        title = title.replace('judgement', 'judgment')
    # super mario bros 2 lost levels
    elif title == 'super mario bros. 2 - the lost levels':
        title = 'super-mario-bros-2-japanese'
    
    # rusn'n attaack
    elif 'rushn' in title:
        title = title.replace('n', '-n')
    
    # the adventures of rocky and bullwinkle
    elif 'rocky' in title:
        title = 'the adventures of ' + title
    
    # Rad Racket: Deluxe Tennis II
    elif title == 'rad racket deluxe tennis 2':
        title = 'rad racket deluxe tennis ii'
    
    #Q*bert
    elif title == 'q*bert':
        title = 'qbert'
    # mr dream's punchout
    elif title == 'punch-out!!':
        title += '-mr-dream'
    
    # puglsleys scavenger hunt
    elif 'pugsley' in title:
        title = 'the addams family ' + title
    
    # mario bros. original
    elif title == 'mario bros.':
        title += ' original'

    # NES play action footbal
    elif title == 'play action football':
        title = 'nes ' + title

    # a nightmare on elm street
    elif title == 'nightmare on elm street':
        title = 'a ' + title

    # A boy and his blob
    elif 'blob' in title:
        title = 'a-boy-and-his-blob'
    # DinoRiki
    elif 'riki' in title:
        title = 'adventures-of-dino-riki'
        
    # 3-D Battles of World Runner, The
    elif '3-d' in title:
        title = '3d-battles-of-worldrunner'
    # Thrilla's Surfari - T and C II
    elif 'thrillas' in title:
        title = 'tc-surf-designs-thrillas-surfari'
    
    # T and C Surf Designs: Wood and Water Rage
    elif 't and c' in title:
        title = 't-and-c-surf-designs'

    # chip n dale 1/2
    elif 'chip' in title:
        title = title.split(', ')
        title = ' '.join((title[1], title[0]))
    
    # Ghost Lion
    elif ', legend of' in title:
        title = 'the-legend-of ' + title.replace(', legend of', '')
    
    # stupid fisher price games
    elif 'fisher-price' in title:

        if ' - fisher-price' in title:
            title = title.split(' - ')
            title = ' '.join((title[1], title[0]))

        elif ', fisher-price' in title:
            title = title.split(', ')
            title = ' '.join((title[1], title[0]))
    
    # super jeopardy!
    elif 'jeopardy! super' in title:
        title = 'super-jeopardy'

    # the jungle book
    elif 'jungle' in title:
        title = 'disneys-the-jungle-book'

    # King of the Ring - WWF
    elif ' - wwf' in title:
        title = title.split(' - ')
        title = ' '.join((title[1], title[0]))

    # replaces the rest
    title = title.replace(',','').replace('.', '').replace('!', '').replace(' / ', '-').replace('/', '-').replace('(', '').replace(')', '').replace('*', '-').replace(' - ', '-').replace(' ', '-').strip(' ')
    
    # for testing
    print title
    
    link = 'http://nesguide.com/games/' + title
    url = urllib2.urlopen(link)
    html = url.read()
    soup = BeautifulSoup(html).find(id="descript")
    description = soup.get_text()
    
    return description


# looks up the amazon game
# returns a single product object
def fetch_from_amazon(game):
    title = ''.join(('NES ', game.title))
    
    AMAZON_ACCESS = os.environ['AMAZON_ACCESS']
    AMAZON_SECRET = os.environ['AMAZON_SECRET']
    AMAZON_AWS = os.environ['AMAZON_AWS']
    
    amazon = AmazonAPI(AMAZON_ACCESS, AMAZON_SECRET,AMAZON_AWS)
    try:
        products = amazon.search_n(1, Keywords=title, Condition='Used', SearchIndex = 'VideoGames')
        return amazon.lookup(ItemId=products[0].asin, Condition='Used')
    
    # if above fails the template handles the error
    except:
        pass

# fetches all games in the DB
def fetch_games():
    return Game.objects.all()


# fetches owned games for the user
def fetch_owned(user):
    owned_games = []
    owned_ids = []
    owned = OwnedGame.objects.filter(user_id=user.id)

    for own in owned:
        owned_ids.append(own.game_id)

    for game in Game.objects.all():
        if game.id in owned_ids:
            owned_games.append(game)

    return owned_games
    


# fetches beaten games for the user
def fetch_beaten(user):
    beaten_games = []
    beaten_ids = []
    beaten = BeatenGame.objects.filter(user_id=user.id)
    
    for beat in beaten:
        beaten_ids.append(beat.game_id)

    for game in Game.objects.all():
        if game.id in beaten_ids:
            beaten_games.append(game)

    return beaten_games


# returns a google search link to be used in templates
def create_google_url(game):
    return (''.join(('https://www.google.com/#q=nes+', str(game.title).replace(' ','+'))))

# creates and returns a string for searching api's
# ex: 'nes+mega+man+2'
def create_search_string(game):
    return (''.join(('nes+', str(game.title).replace(' ','+'))))
    
    
# ******************************************* #
# filter_games()                              #
# filters all games by passed in filters from #
# random.html form arguments                  #
# games: a list of game objects               #
# params: a dict of parameters                #
# games_owned: a list of owned game objects   #
# beaten_games: a list of beaten game objects #
# returns a filters list of game objects      #
# ******************************************* #
def filter_games(all_games, params, games_owned, beaten_games):
    
    games = list(all_games)
    
    # master loop
    for game in all_games:
        remove = False # master remove variable

        # removes games that user does not own if an argument
        if params['selection'] == 'owned':
            
            not_owned = True
            for owned in games_owned:
                if game.id == owned.game_id:
                    not_owned = False
            if not_owned:
                remove = True

    
        # removes games that don't match the genre if selected
        if params['genres']:

            if game.genre not in params['genres']:
                remove = True
           
        # checks if user set the beaten filter
        if params['beaten'] != 'both':
            
            # Beaten = 'Yes' in the random form
            if params['beaten'] == 'yes':
                beaten = False
                for beaten_game in beaten_games:
                    if game.id == beaten_game.game_id:
                        beaten = True
                if not beaten:
                    remove = True
                        
                        
            # Beaten = 'Yes' in the random form
            elif params['beaten'] == 'no':
                for beaten_game in beaten_games:
                    if game.id == beaten_game.game_id:
                        remove = True
                        break
                
        if remove:
            games.remove(game)

    return games
# end filter_games() #