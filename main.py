import sentiment_analysis as sa

tweetsFile = input("Enter the name of the file containing tweets: ")
keywordsFile = input("Enter the name of the file containing keywords and value: ")

resultList = sa.compute_tweets(tweetsFile, keywordsFile)

print("Eastern region:")
print("Happiness average:", resultList[0][0])
print("Keywords count:", resultList[0][1])
print("Tweets count:", resultList[0][2])
print()
print("Central region:")
print("Happiness average:", resultList[1][0])
print("Keywords count:", resultList[1][1])
print("Tweets count:", resultList[1][2])
print()
print("Mountain region:")
print("Happiness average:", resultList[2][0])
print("Keywords count:", resultList[2][1])
print("Tweets count:", resultList[2][2])
print()
print("Pacific region:")
print("Happiness average:", resultList[3][0])
print("Keywords count:", resultList[3][1])
print("Tweets count:", resultList[3][2])
print()



