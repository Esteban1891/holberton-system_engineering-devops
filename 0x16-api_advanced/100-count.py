#!/usr/bin/python3
"""A file to make a query to an endpoint"""
from requests import request


def count_words(subreddit, word_list, after="", counter={}, ini=0):
    """A recursive function that queries the Reddit API, parses the title
    of all hot articles, and prints a sorted count of given keywords
    (case-insensitive, delimited by spaces. Javascript should count as
    javascript, but java should not)
    """
    if ini == 0:
        for word in word_list:
            counter[word] = 0

    url = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, after)
    headers = {"User-Agent": "Python3"}
    response = request("GET", url, headers=headers).json()
    try:
        top = response['data']['children']
        _after = response['data']['after']
        for item in top:
            for word in counter:
                counter[word] += item['data']['title'].lower(
                    ).split(' ').count(word.lower())
        if _after is not None:
            count_words(subreddit, word_list, _after, counter, 1)
        else:
            str = sorted(counter.items(), key=lambda kv: kv[1], reverse=True)
            for name, num in str:
                if num != 0:
                    print('{}: {}'.format(name, num))
    except Exception:
        return None
