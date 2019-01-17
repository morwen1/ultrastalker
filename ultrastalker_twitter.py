import tweepy
from textblob import TextBlob
import pandas as pd
import psycopg2
import time
class UtlrastalkerTwitter():
    def __init__(self):
        self.consumer_key = 'MXxkjXdFDVsZ0nZHZP5pQ7ZRl'
        self.consumer_secret = 'WacadTfwtATEonKfH0zdZYO0rERkKeVmIvKC0mgkchs1fkLyXU'
        self.acces_token = '830475844141322240-Lzvz5a59yNngZYUwoJUrmYNHvZ2aYK0'
        self.acces_token_secret = 'c4fJkuPbLi4x6U1cXtoGW1ZmpRu6lHlupb408TupWOiRH'
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.acces_token, self.acces_token_secret)
        self.api = tweepy.API(self.auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

    def generic_search(self, item_to_search):
        self.public_tweets = self.api.search('item_to_search')
        self.sentiment = []
        self.public_tweets1 = []
        print(self.public_tweets)
        for tweet in self.public_tweets:
            print(tweet.text)

            self.analysis = TextBlob(str(self.tweet.text))
            self.analysis.translate(from_lang='es' , to='en')
            print(analysis.sentiment,"analisis")
            self.public_tweets1.append(self.weet.text)
            self.sentiment.append(self.analysis.sentiment)

        self.data = {'sentiments': self.sentiment, 'twitts': self.public_tweets1}

    def user_search(self, usr):
        self.user = self.api.get_user(str(usr))



        print('usuario : ',self.user.screen_name)
        print('Cant-Seguidores : ',self.user.followers_count)
        self.locacion_pos_followers = []
        self.name_followers = []
        self.screen_name = []
        for us in tweepy.Cursor(self.api.followers, id=usr, count=30).items():
            #self.page_count += 1
            #print ('Getting page {} for followers'.format(self.page_count))
            if us.location == '' :
                us.location='N/A'
            if us.name =='':
                us.name ='N/A'
            print(us.location ,'\t',us.name,',',us.screen_name)
            self.locacion_pos_followers.append(us.name)
            self.name_followers.append(us.location)
            self.screen_name.append(us.screen_name)


        self.timeline = self.api.user_timeline




        cursor = tweepy.Cursor(self.timeline,id=usr)
        self.timeline = []
        self.sentiment= []
        self._=0
        for i in cursor.items(limit=self.user.followers_count):

            self.analysis = TextBlob(i.text)
            self.timeline.append(i.text)
            try:
               if self.analysis.detect_language() != 'en' :
                   self.analysis= self.analysis.translate(from_lang=self.analysis.detect_language(), to='en' )
                   self.sentiment.append(self.analysis.sentiment)
               else:
                    self.sentiment.append(self.analysis.sentiment)
            except Exception as e:
               self.sentiment.append(e)
            if i.text == '' :
                self.timeline.append('N/A')
                self.sentiment.append('N/A')
                continue
            print(self.sentiment[self._],i.text)
            #self.timeline.append(i.text)
            #self.sentiment.append(self.analysis.sentiment)
            self._ += 1
        self.dffollowers = pd.DataFrame(
            {'Followers.name' : self.name_followers,
             'followers.screen_name': self.screen_name,
             'Followers.Loc' : self.locacion_pos_followers,

             })
        print(len(self.timeline))
        print(len(self.sentiment))
        self.dftimeline = pd.DataFrame({
           'timeline_twits': self.timeline,
           'timeline.sentiment.twitts': self.sentiment,
       	})
        print(self.dffollowers.head(10))
        print(self.dftimeline.head(10))
        self.dftimeline.to_csv(usr+'_timeline'+'.csv')
        self.dffollowers.to_csv(usr+'_followers'+'.csv')
        return


dec = True
while dec:

	print("""

	 █    ██  ██▓  ▄▄▄█████▓ ██▀███   ▄▄▄                      
	 ██  ▓██▒▓██▒  ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄                    
	▓██  ▒██░▒██░  ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄                  
	▓▓█  ░██░▒██░  ░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██                 
	▒▒█████▓ ░██████▒▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒                
	░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░                
	░░▒░ ░ ░ ░ ░ ▒  ░  ░      ░▒ ░ ▒░  ▒   ▒▒ ░                
	 ░░░ ░ ░   ░ ░   ░        ░░   ░   ░   ▒                   
	   ░         ░  ░          ░           ░  ░                
	                                                           
	  ██████ ▄▄▄█████▓ ▄▄▄       ██▓     ██ ▄█▀▓█████  ██▀███  
	▒██    ▒ ▓  ██▒ ▓▒▒████▄    ▓██▒     ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
	░ ▓██▄   ▒ ▓██░ ▒░▒██  ▀█▄  ▒██░    ▓███▄░ ▒███   ▓██ ░▄█ ▒
	  ▒   ██▒░ ▓██▓ ░ ░██▄▄▄▄██ ▒██░    ▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
	▒██████▒▒  ▒██▒ ░  ▓█   ▓██▒░██████▒▒██▒ █▄░▒████▒░██▓ ▒██▒
	▒ ▒▓▒ ▒ ░  ▒ ░░    ▒▒   ▓▒█░░ ▒░▓  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
	░ ░▒  ░ ░    ░      ▒   ▒▒ ░░ ░ ▒  ░░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
	░  ░  ░    ░        ░   ▒     ░ ░   ░ ░░ ░    ░     ░░   ░ 
	      ░                 ░  ░    ░  ░░  ░      ░  ░   ░     
	                                                           

	            v0.0.0.1
	           TR4NS1STH0R
	""")
	objeto = UtlrastalkerTwitter()

	print('busqueda por usuario o en general ')
	print('gen : general  \t usr : usuario')
	dec= str(input('>> '))
	if dec == 'gen' :
		objeto.generic_search(input('introduce el twitt'))
	if dec == 'usr':
		objeto.user_search(input('introduce el usuario'))
	
	if dec == 'cancel':
		dec=False
		break
