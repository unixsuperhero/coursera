import sys
import json
import re

def hw(sent_file, tweet_file):
    sentiments = get_sentiments(sent_file)
    tweets = get_tweets(tweet_file)
    for t in tweets:
        words = get_words(t)
        print sent_value(words, sentiments)

def sent_value(words, sentiments):
    v = 0
    for w in words:
        if w in sentiments:
            v += sentiments[w]
    return float(v)

def get_words(t):
    return re.split("\W\W*", t)

def get_sentiments(f):
    scores = {}
    for line in f:
        t,s = line.split("\t")
        scores[t] = int(s)
    return scores

def get_tweets(f):
    tweets = []
    for line in f:
        tweet = json.loads(line)
        tweets.append(tweet["text"])
    return tweets

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()
