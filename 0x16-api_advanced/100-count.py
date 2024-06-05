#!/usr/bin/python3
"""
Module to recursively query the Reddit API and count occurrences of keywords in hot article titles.
"""

import requests
from collections import Counter

def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Recursively queries the Reddit API, parses the titles of all hot articles,
    and prints a sorted count of given keywords.
    
    :param subreddit: The subreddit to query.
    :param word_list: List of keywords to count.
    :param after: The pagination parameter for the Reddit API.
    :param word_count: Dictionary to store the count of keywords.
    """
    if word_count is None:
        word_count = Counter()
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'myAPI/0.0.1'}
    params = {'limit': 100, 'after': after}
    
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        if response.status_code != 200:
            return
        
        data = response.json()
        articles = data['data']['children']
        
        for article in articles:
            title = article['data']['title'].lower().split()
            for word in word_list:
                word = word.lower()
                word_count[word] += title.count(word)
        
        after = data['data']['after']
        if after is not None:
            count_words(subreddit, word_list, after, word_count)
        else:
            sorted_word_count = sorted(word_count.items(), key=lambda item: (-item[1], item[0]))
            for word, count in sorted_word_count:
                if count > 0:
                    print(f"{word}: {count}")
    
    except requests.RequestException:
        return
