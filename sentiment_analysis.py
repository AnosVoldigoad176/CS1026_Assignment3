# Key and Value formatter for original line from keywords
def kvFormat(line):
    keywordAndValue = line.strip().split(",")  # Ensure no trailing space and set separator at ","
    return keywordAndValue


# Tweet formatter for original line of tweets
def twFormat(line):
    tweet = line.strip().split()  # Ensure no trailing space and default separator blank space

    # Format coordinates of tweets ONLY
    tweet[0] = float(tweet[0].strip("[,"))
    tweet[1] = float(tweet[1].strip("]"))

    # Format everything after coordinates
    for i in range(2, len(tweet)):
        tweet[i] = tweet[i].strip("!\"#$%&'()*+, -./:;<=>?@[\]^_`{|}~").lower()  # Remove punctuation and make words lowercase

    return tweet


# Set region for tweets
def setRegion(tweet):
    region = ""

    # Index 0 = lat, 1 = long
    p1 = [49.189787, -67.444574]
    p3 = [49.189787, -87.518395]
    p5 = [49.189787, -101.998892]
    p7 = [49.189787, -115.236428]
    p9 = [49.189787, -125.242264]

    p2 = [24.660845, -67.444574]
    p4 = [24.660845, -87.518395]
    p6 = [24.660845, -101.998892]
    p8 = [24.660845, -115.236428]
    p10 = [24.660845, -125.242264]

    # Check if the tweet in CONUS
    if p1[0] >= tweet[0] >= p2[0] and p1[1] >= tweet[1] >= p9[1]:




def compute_tweets(tweetsFile, keywordsFile):
    try:
        tweets = open(tweetsFile, "r")
        keywords = open(keywordsFile, "r")

    except FileNotFoundError:
        print("File not found")
