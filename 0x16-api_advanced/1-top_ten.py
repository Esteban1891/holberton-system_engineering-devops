#!/usr/bin/python3
"""
Queries the Reddit API and prints the first ten hot posts for a given subreddit
"""
import requests


def top_ten(subreddit):
    posts = ""
    if (type(subreddit) is not str):
        posts = "None\n"
    else:
        api_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        headers = {'user-agent': 'safari:holberton/0.1.0'}
        response = requests.get(api_url, headers=headers)
        if response.status_code is not 200:
            posts = "None\n"
        else:
            posts_json = response.json().get("data").get("children")
            for i in range(10):
                post_title = posts_json[i].get("data").get("title")
                posts += "{}\n".format(post_title)
    print(posts, end="")
