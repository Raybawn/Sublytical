import praw
import os

import re
import emoji
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

reddit = praw.Reddit("bot1", config_interpolation="basic")

userinput = input("Enter subreddit:")
subreddit = reddit.subreddit(userinput)

postLimit = 100
postList = []
wordList = []
postWords = []
wordString = ""

for submission in subreddit.hot(limit=postLimit):
    postList.append([submission.title])
    postWords = list(set(word_tokenize(submission.title.lower().replace("'", ""))))
    wordList.extend(postWords)

stops = set(stopwords.words("english"))  # Filter out stopwords (the, a, is, etc.)
nonPunct = re.compile(".*[A-Za-z0-9].*")  # Filter out non-alphanumeric characters


def remove_emoji(str):
    return emoji.replace_emoji(str, replace="")  # Filter out emojis


wordList = [remove_emoji(w) for w in wordList if not w in stops and nonPunct.match(w)]

for word in wordList:
    wordString += str(word + " ")

wordString = wordString[:-1]

print(wordString)
