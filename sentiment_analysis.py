# Key and Value formatter for original line from keywords
def kvFormat(line):
    keywordAndValue = line.strip().split(",")  # Ensure no trailing space and set separator at ","
    return keywordAndValue


# Tweet formatter for original line of tweets
def twFormat(line):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    tweet = line.strip().split()  # Ensure no trailing space and default separator blank space

    # Format coordinates of tweets ONLY
    for i in range(0, 2):
        tweet[i] = tweet[i].strip("[,]")  # Remove punctuation
    tweet[0] = float(tweet[0])  # Remove "[" at the beginning of latitude and "," at the end
    tweet[1] = float(tweet[1])  # Remove "]" at the end of longtitude

    # Format everything after coordinates
    for i in range(2, len(tweet)):
        tweet[i] = tweet[i].strip(punc).lower()  # Remove punctuation and make words lowercase

    return tweet


# Set region for tweets
def setRegion(tweet):
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

    region = ""

    # Check if the tweet in CONUS
    if 49.189787 >= tweet[0] >= 24.660845 and -67.444574 >= tweet[1] >= -125.242264:
        if p1[1] >= tweet[1] > p3[1]:  # Check if the longtitude is in [p1,p3)
            region = "Eastern"
        elif p3[1] >= tweet[1] > p5[1]:  # Check if the longtitude is in [p3,p5)
            region = "Central"
        elif p5[1] >= tweet[1] > p7[1]:  # Check if the longtitude is in [p5,p7)
            region = "Mountain"
        elif p7[1] >= tweet[1] >= p9[1]:  # Check if the longtitude is in [p7,p9]
            region = "Pacific"

    return region


def scoreCalc(tweet, keywordsAndValues):
    score = 0
    kwFound = 0

    # Loop exclude everything before tweets
    for i in range(5, len(tweet)):
        if tweet[i] in keywordsAndValues and tweet[i].isalpha():  # Check if word is in keyword and it's not number
            kwIndex = keywordsAndValues.index(tweet[i])  # Get index of the keyword from the keyword list
            score += int(keywordsAndValues[kwIndex + 1])  # Next to the index of keyword is value
            kwFound += 1

    if score == 0:
        return 0
    else:
        return score / kwFound


def compute_tweets(tweetsFile, keywordsFile):
    # Tweet counter variables per region
    easternTw = 0
    centralTw = 0
    mountainTw = 0
    pacificTw = 0

    # Keyword counter variables per region
    easternKw = 0
    centralKw = 0
    mountainKw = 0
    pacificKw = 0

    # Score counter variables per region
    easternScr = 0
    centralScr = 0
    mountainScr = 0
    pacificScr = 0

    keywordsAndValues = []

    try:
        tweets = open(tweetsFile, "r", encoding="utf-8")
        keywords = open(keywordsFile, "r", encoding="utf-8")

        # Read keywords file
        for line in keywords:
            for index in kvFormat(line):
                keywordsAndValues.append(index)

        # Go one by one till the end of the file
        for line in tweets:
            tweet = twFormat(line)  # Run line formatter
            region = setRegion(tweet)  # Run region getter

            if region == "Eastern":
                easternTw += 1
                if scoreCalc(tweet, keywordsAndValues) != 0:
                    easternKw += 1
                    easternScr += scoreCalc(tweet, keywordsAndValues)
            elif region == "Central":
                centralTw += 1
                if scoreCalc(tweet, keywordsAndValues) != 0:
                    centralKw += 1
                    centralScr += scoreCalc(tweet, keywordsAndValues)
            elif region == "Mountain":
                mountainTw += 1
                if scoreCalc(tweet, keywordsAndValues) != 0:
                    mountainKw += 1
                    mountainScr += scoreCalc(tweet, keywordsAndValues)
            elif region == "Pacific":
                pacificTw += 1
                if scoreCalc(tweet, keywordsAndValues) != 0:
                    pacificKw += 1
                    pacificScr += scoreCalc(tweet, keywordsAndValues)

        if easternKw != 0:
            easternScr /= easternKw
        if centralKw != 0:
            centralScr /= centralKw
        if mountainKw != 0:
            mountainScr /= mountainKw
        if pacificKw != 0:
            pacificScr /= pacificKw

        resultList = [(easternScr, easternKw, easternTw), (centralScr, centralKw, centralTw),
                      (mountainScr, mountainKw, mountainTw), (pacificScr, pacificKw, pacificTw)]

        tweets.close()
        keywords.close()

        return resultList

    except FileNotFoundError:
        print("File not found")
        return [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]
