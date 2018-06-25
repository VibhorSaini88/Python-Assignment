#(Q.1)- What is an access token? Generate your access token for any API.(for example Twitter,Spotify etc).

Ans:- An access token is an object that describes the security context of a process or thread. The information in a token includes the identity and privileges of the user account associated with the process or thread. When a user logs on, the system verifies the user's password by comparing it with information stored in a security database. If the password is authenticated, the system produces an access token. Every process executed on behalf of this user has a copy of this access token.
								consumer_key88='  '
								consumer_secrete88=' '
								access_token88=' '
								access_token_secrete88=' '
								

#(Q.2)- Get the IP address of some common sites like Google, Facebook by using DNS lookup.

C:\Users\Vibhor saini>nslookup facebook.com
Server:  UnKnown
Address:  192.168.43.1

Non-authoritative answer:
Name:    facebook.com
Addresses:  2a03:2880:f10c:283:face:b00c:0:25de
          157.240.13.35


C:\Users\Vibhor saini>nslookup google.com
Server:  UnKnown
Address:  192.168.43.1

Non-authoritative answer:
Name:    google.com
Addresses:  2404:6800:4002:806::200e
          172.217.26.238


#(Q.3)- Using Tweepy library try to extract tweets from Twitter.
import tweepy

consumer_key88=' '
consumer_secrete88=' '
access_token88=' '
access_token_secrete88=' '
auth=tweepy.OAuthHandler(consumer_key88,consumer_secrete88)
auth.set_access_token(access_token88,access_token_secrete88)
api=tweepy.API(auth)
tweets=api.search("#notwithoutmydog",lang="en",count='5',tweet_mode="extended")

#print(tweets)

for tweet in tweets:
	print("--------------")
	print("tweet.full_text")
	print("-------------------")
	
	
#(Q.4)- What is a difference between library and API . Figure it out with examples.
  Ans:- Library = A library is a collection of functions / objects that serves one particular purpose. you could use a library in a variety of projects. (Various specialized services in our case).

  API = An API is an interface for other programs to interact with your program or library  without having direct access. ( giving specifications for our need to various vendors in our case).
  
