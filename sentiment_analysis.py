def compute_tweets(tweets, key):
    try:
        tweetsFile = open(tweets, "r")
        keyFile = open(key, "r")
    except FileNotFoundError:
        print('File not found.')


