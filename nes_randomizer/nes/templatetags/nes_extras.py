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
    if re.search(', \w* \w*\'s', title, flags=re.IGNORECASE):
        title = title.split(', ')
        title = ' '.join((title[1], title[0]))

    title = title.replace(':','').replace('IV', '4').replace('III','3').replace('II','2').replace('\'','').replace('\&','and').replace(' - ', ' ').lower()
    
    #corner cases
    # Thrilla's Surfari - T and C II
    if 'thrillas' in title:
        title = 'tc-surf-designs-thrillas-surfari'
    
    # T and C Surf Designs: Wood and Water Rage
    if 't and c' in title:
        title = 't-and-c-surf-designs'
    
    if ', disneys' in title:
        title = title.split(', ')
        title = ' '.join((title[1], title[0]))
    if ', the' in title:
        title = 'the ' + title.replace(', the', '')
    if ', legend of' in title:
        title = 'the-legend-of ' + title.replace(', legend of', '')
    if 'fisher-price' in title:
            if '- fisher-price' in title:
                title = title.split(' - ')
                title = title[1] + ' ' + title[0]
            else:
                title = title.split(', ')
                title = ' '.join((title[1], title[0]))
    
    # replaces the rest
    title = title.replace(',','').replace(' ', '-').replace('.', '').replace('!', '')
    
    # for testting
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
def fetch_games(request):
    return Game.objects.all()

# fetches owned games for the user
def fetch_owned(request):
    return OwnedGame.objects.filter(user_id=request.user.id)

# fetches beaten games for the user
def fetch_beaten(request):
    return BeatenGame.objects.filter(user_id=request.user.id)

# returns a google search link to be used in templates
def create_google_url(game):
    return (''.join(('https://www.google.com/#q=nes+', str(game.title).replace(' ','+'))))

# creates and returns a string for searching api's
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

    # removes games that user does not own if an argument
    if params['selection'] == 'owned':
        
        for game in all_games:
            not_owned = True
            for owned in games_owned:
                if game.id == owned.game_id:
                    not_owned = False
                    break
            if not_owned:
                games.remove(game)

    # removes games that don't match the genre if selected
    if params['genres']:
        
        # # start testing crap
        # print '\nPARAMS:'
        # for param in params['genres']:
            # print param
        # print '\n'
        # # end testing crap
        
        for game in all_games:
            if game in games and game.genre not in params['genres']:
                games.remove(game)
                # print 'removing: %s' % game.title
    
    # checks if user set the beaten filter
    if params['beaten'] != 'both':
        beaten = (True if params['beaten']  == 'yes' else False)
        # if params['beaten'] == 'yes':
        for game in all_games:

            # beaten filter = true, remove games that are not on list
            if beaten:
                beat = False
                for beaten_game in beaten_games:
                    if game.id == beaten_game.game_id:
                        beat = True
                if game in games and not beat:
                    games.remove(game)
                    
            # beaten filter = false, remove games taht are on list
            if not beaten:
                beat = False
                for beaten_game in beaten_games:
                    if game in games and game.id == beaten_game.game_id:
                        games.remove(game)
                
    
    
    return games
# end filter_games() #