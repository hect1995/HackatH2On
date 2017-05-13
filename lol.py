from twitter import *
import os
import oauth
import tweepy
from tweepy import OAuthHandler
import json
from tweepy import Stream
from tweepy.streaming import StreamListener
#import dataset  #per guardar els fichers en una BD
import time,threading  #l'utilitzare per fer que cada 10 segons s'executi el mirar si hi han nous tweets
from twython import Twython  #importar Twython
from tweepy import Stream
from tweepy import API
import random
import numpy as np

#Create a new Twitter app first: https://apps.twitter.com/app/new


APP_KEY,APP_SECRET = 'H3kQtN5PQgRiA0ocRCCjqjt2P', '51UaJFdEally81B7ZXjGHkDoDKTYy430yd1Cb0St5Hb1BVcDfE'
# OAUTH_TOKEN, OAUTH_TOKEN_SECRET = '149655407-TyUPMYjQ8VyLNY5p7jq0aMy8PjtFtd7zkIpDh3ZA', 'IUVpiDpoVmdO75UaHOTinAv5TOsAQmddttNENh9ofYuWO'

consumer_key = 'vfnSAB7waXE2OAu7MtUUIbTTo'  # tot aixo es necesari per connectarnos a la conta de twitter d'Alvaro
consumer_secret = 'SiSSrKHuplyeSyHWsgfEYJYjrCnsntaLPza10rHfaxBVZNPdUb'
access_token = '861315124459704320-85K9LhrkTlwNexJacKK7a4k0ZywNkGy'
access_secret = 'C3UAenDtpBRiKNREod1gughfNp2PtCITF2v21GLUNNCDP'



def resposta(u_id, case):

    if not converses.has_key(u_id):
        converses[u_id] = [case]
    else:
        converses[u_id].append(case)


    if converses[u_id][0] == 0 :
        if len(converses[u_id]) > 1 :
            if converses[u_id][1] == 0:
                lola = api1.send_direct_message(user_id=u_id,
                                                text="1 - Qui som. \n2 - Centres i Instalacions. \n 3 - Consum Global. \n4 - Calitat de l'aigua. \n5 - Compromis Social i Sostenibilitat. \n6 - Noticies, Premsa\n")  # -->enviar missatge
            elif converses[u_id][1] == 1:
                lola = api1.send_direct_message(user_id=u_id,
                                                text="1 - Averies. \n2 - Facturacio. \n 3 - Tarifes i Impostos. \n4 - Altes, Baixes, Canvis de Titularitat. \n5 - Promocions. \n6 - Canals de Pagament\n")  # -->enviar missatge
            elif converses[u_id][1] == 2:
                lola = api1.send_direct_message(user_id=u_id,
                                               text="1 - Errors. \n2 - Incidencies. \n")  # -->enviar missatge

        else:
            lola = api1.send_direct_message(user_id=u_id, text="1 - Informacio General. \n2 - Serveis. \n 3 - Reclamacions.\n")  # -->enviar missatge

    elif converses[u_id][0] == 1 :
        if len(converses[u_id])>1:
            if converses[u_id][1] == 0:
                lola = api1.send_direct_message(user_id=u_id,
                                                text="1 - Qui som. \n2 - Centres i Instalacions. \n 3 - Consum Global. \n4 - Calitat de l'aigua. \n5 - Compromis Social i Sostenibilitat. \n6 - Noticies, Premsa\n")  # -->enviar missatge
            elif converses[u_id][1] == 1:
                lola = api1.send_direct_message(user_id=u_id,
                                                text="1 - Averies. \n2 - Facturacio. \n 3 - Tarifes i Impostos. \n4 - Altes, Baixes, Canvis de Titularitat. \n5 - Promocions. \n6 - Canals de Pagament\n")  # -->enviar missatge
            elif converses[u_id][1] == 2:
                lola = api1.send_direct_message(user_id=u_id,
                                               text="1 - Errors. \n2 - Incidencies. \n")  # -->enviar missatge

        else:
            lola = api1.send_direct_message(user_id=u_id, text="1 - Informacio General. \n2 - Serveis. \n 3 - Reclamacions.\n")  # -->enviar missatge


    elif converses[u_id][0] ==2 :
        if len(converses[u_id])>1:
            if converses[u_id][1] == 0:
                lola = api1.send_direct_message(user_id=u_id,
                                                text="1 - Qui som. \n2 - Centres i Instalacions. \n 3 - Consum Global. \n4 - Calitat de l'aigua. \n5 - Compromis Social i Sostenibilitat. \n6 - Noticies, Premsa\n")  # -->enviar missatge
            elif converses[u_id][1] == 1:
                lola = api1.send_direct_message(user_id=u_id,
                                                text="1 - Averies. \n2 - Facturacio. \n 3 - Tarifes i Impostos. \n4 - Altes, Baixes, Canvis de Titularitat. \n5 - Promocions. \n6 - Canals de Pagament\n")  # -->enviar missatge
            elif converses[u_id][1] == 2:
                lola = api1.send_direct_message(user_id=u_id,
                                               text="1 - Errors. \n2 - Incidencies. \n")  # -->enviar missatge

        else:
            lola = api1.send_direct_message(user_id=u_id, text="1 - Informacio General. \n2 - Serveis. \n 3 - Reclamacions.\n")  # -->enviar missatge
    print(converses)
auth1 = OAuthHandler(consumer_key, consumer_secret)  # per permetre accedir a Twitter desde Python
auth1.set_access_token(access_token, access_secret)  # per permetre accedir a Twitter desde Python"""
api1 = tweepy.API(auth1)  # per permetre accedir a Twitter desde Python

class StdOutListener( StreamListener ):
    def __init__( self ):
        self.tweetCount = 0

    def on_connect( self ):
        print("Connection established!!")

    def on_disconnect( self, notice ):
        print("Connection lost!! : ", notice)

    def on_data( self, status ):
        print("Entered on_data()")
        print status
        #if i==0 :
        #if not status.find('{"friends":[',0,len(status)):
        if '{"friends":[' in status:

            print(0)
        else: #"""status.find('{"direct_message"',0,50):"""
            if not '"sender":{"id":861315124459704320' in status:
                print ("HELLO")
                sender= status.find('"sender":{"id":') #length=14
                final=status.find(',"id_str"', sender)
                user_id= (status[sender+len('"sender":{"id":'):final])
                print list

        # print(str(status['direct_message']))
        #print(status['direct_message']['sender']['id'])
                resposta(int(user_id),random.randint(0,2))
        return True

    def on_direct_message( self, status ):
        print("Entered on_direct_message()")
        try:
            print(status)
            return True
        except BaseException as e:
            print("Failed on_direct_message()", str(e))

    def on_error( self, status ):
        print(status)


converses={}


stream = Stream(auth1, StdOutListener())
stream.userstream()







""""
#stream = Stream(auth, StdOutListener())
#stream.userstream()
MY_TWITTER_CREDS = os.path.expanduser('my_app_credentials')
if not os.path.exists(MY_TWITTER_CREDS):
    oauth_dance("crypto sentiments", APP_KEY, APP_SECRET,
                MY_TWITTER_CREDS)

oauth_token, oauth_secret = read_token_file(MY_TWITTER_CREDS)"""

"""auth = OAuth(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    token=access_token,
    token_secret=access_secret
)

auth = OAuthHandler(consumer_key, consumer_secret)  #per permetre accedir a Twitter desde Python
auth.set_access_token(access_token, access_secret)  #per permetre accedir a Twitter desde Python
api = tweepy.API(auth)                              #per permetre accedir a Twitter desde Python
"""
"""
twitter_userstream = TwitterStream(auth=auth, domain='userstream.twitter.com')

for msg in twitter_userstream.user():
    print msg
    print twitter_userstream.user()

    if 'direct_message' in msg:

        #if not api.exists_friendship(msg['direct_message']['sender']['id'],screen_name='HACKH2O_BCN'):
         #   api1.create_friendship(msg['direct_message']['sender']['id'],[0])
        time.sleep(random.randint(0,5))
        #print (msg['direct_message']['text'])
        #print (msg['direct_message']['sender']['id'])
        resposta(msg['direct_message']['sender']['id'],random.randint(0,5))

        #lola = api.send_direct_message(user_id=missatge, text='LOL Por Fin')  # -->enviar missatge

"""

