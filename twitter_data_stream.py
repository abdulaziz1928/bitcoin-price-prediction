from statistics import mean
import tweepy
import preprocessor as p
from stop_words import get_stop_words
from textblob import TextBlob
import numpy as np


def main():
    # set twitter api credentials
    consumer_key = 'aHYihqacTLrkRqtfh1dywbX21'
    consumer_secret = 'GMN8oUbIA4AiQIJlNfXAfs3nwA1nOIBtbGRVJzFNKgu5jPsKvj'
    access_token = '326361938-za3nzmaodrWW2SKgIBQYPZG7CPopRnuGYbJpHPRI'
    access_token_secret = 'b1xkl6xZCvICMfpTKd4JVmiYjR7BCMFpUxjNublu69m7y'

    # initilize tweepy
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    twitter_api = tweepy.API(auth)

    # Get tweets related to keywords
    tweets = twitter_api.search_tweets("bitcoin", count=4)

    # Prepocessing
    cleaned_tweets = clean_tweets(tweets)
    for tweet in cleaned_tweets:
        print(tweet)
    cleaned_tweets = remove_stop_words(cleaned_tweets)

    print("-------------------")
    for tweet in cleaned_tweets:
        print(tweet)

    polarity = get_polarity(cleaned_tweets)
    for p in polarity:
        print(p)

    m = np.mean(polarity)
    print(m)


# Cleans the tweets by removing the following:
# URL, Mention, Hashtag, Reserved Words, Emoji, Smiley, Number
def clean_tweets(tweets):
    return [p.clean(tweet.text) for tweet in tweets]


def remove_stop_words(tweets):
    processed_tweets = []
    for tweet in tweets:
        clened_text = ' '.join(
            [word for word in tweet.split() if word not in get_stop_words('english')])
        processed_tweets.append(clened_text)
    return processed_tweets


def get_polarity(tweets):
    polarities = []
    for tweet in tweets:
        res = TextBlob(tweet)
        polarities.append(res.sentiment.polarity)
    return polarities


main()
