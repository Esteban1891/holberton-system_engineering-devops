#!/usr/bin/python3
"""
Querying the Reddit API recursively
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    if type(subreddit) is not str:
        return None
    sub = subreddit
    api_url = "https://api.reddit.com/r/{}/hot?after={}".format(sub, after)
    headers = {'user-agent': 'safari:holberton/0.1.0'}
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        hot_posts = response.json()["data"]["children"]
        after = response.json()["data"]["after"]
        if after is None:
            hot_list = titles(hot_posts, len(hot_posts))
            return hot_list
        hot_list.append(recurse(subreddit, hot_list, after=after))
        hot_list = titles(hot_posts, len(hot_posts))
    else:
        return None
    return hot_list


def titles(hot_list, length, titles_list=[]):
    """
    Gets titles of posts from the data
    """
    if length == 0:
        return titles_list
    titles_list.append(hot_list[length - 1]["data"]["title"])
    return titles(hot_list, length - 1, titles_list)
