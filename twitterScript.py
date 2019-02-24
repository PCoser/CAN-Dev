from TwitterSearch import *
import nltk
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
import json
import praw
import string




reddit = praw.Reddit(client_id='7a1tRqF8QEOrQw',
                     client_secret='Ykjn4zG_ZKTU2d0Zg53TQJ5tIUk',
                     user_agent='statcanapp')




consumer_key = 'gOgoxMbMgY3jtb8HgTxBGyaUR'
consumer_secret = 'Znfm8b9K9jkmNBqEPJPVinLkliaPLIF2zFDIghiXYUezm15Qcn'
access_token = '872577847113768963-zLABqH2riV18Z2pNVVkzusUeuM2tQMC'
access_token_secret = 'WxGvF3LoWgMiCOEhiUeAw8OqRCPBhNBxefKqDaJZgUOBf'


stop_words = set(stopwords.words('english')) 
keywordsToSearch = ['First Nations', 'First Nations Issues', 'First Nations Problems', 'Indigenous Canada', 'Indigenous Problems Canada', 'Indigenous Issues Canada']
#keywordsToSearch = ['First Nations']
dictionaryOfResults={}
uselessWords = ['RT', '@', 'rt', "#", '``', '', ']', '[', ',', '.', '...', '..', '&', '%']
for c in string.punctuation:
    uselessWords.append(c)
listBadStart = ['/', 'http', '\\']


endResultString = ""


for keyword in keywordsToSearch:
  try:
      tso = TwitterSearchOrder() # create a TwitterSearchOrder object
      tso.set_keywords([keyword]) # let's define all words we would like to have a look for
      #tso.set_language('de') # we want to see German tweets only
      tso.set_include_entities(False) # and don't give us all those entity information

      ts = TwitterSearch(
        consumer_key = consumer_key,
        consumer_secret = consumer_secret,
        access_token = access_token,
        access_token_secret = access_token_secret
      )

      #listOfTweets = []

      for tweet in ts.search_tweets_iterable(tso):
          tweetToAppend = ''
          tweetInstance = word_tokenize(tweet['text']) 
          for word in tweetInstance:
            word = word.lower()
            if (word not in stop_words) and (word not in uselessWords) and (not word.startswith(('/', 'http', '\\'))):
              #tweetToAppend += word+" "
              endResultString += word + " "
          #listOfTweets.append(tweetToAppend)
      #dictionaryOfResults[keyword] = listOfTweets
  except TwitterSearchException as e: # take care of all those ugly errors if there are some
      print(e)


# as requested in comment




for keyword in keywordsToSearch:
  #listReddit = []
  for submission in reddit.subreddit('canada').search(keyword):
    subm = word_tokenize(submission.title)
    #redditToAppend=''
    for word in subm:
          if word not in stop_words: #TODO: maybe get rid of @ and # or store them somewhere else
              if(word not in uselessWords):
                  #redditToAppend +=word+" "
                  endResultString += word + " "
    #listReddit.append(redditToAppend)
  #dictionaryOfResults[keyword+'REDDIT'] = listReddit


text_file = open("Output.txt", "w")
text_file.write("%s" % endResultString)
text_file.close()


print("Done")