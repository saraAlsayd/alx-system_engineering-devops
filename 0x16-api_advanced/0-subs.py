#!/usr/bin/python3
"""
This module defines a function to query the Reddit API and return
the number of subscribers for a given subreddit.
"""
import requests

def number_of_subscribers(subreddit):
	 """
    Queries the Reddit API and returns the number of subscribers for
    a given subreddit. If the subreddit is invalid, returns 0.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers or 0 if the subreddit is invalid.
    """
	#Define the Url for the subreddit's info
	url = f"https://www.reddit.com/r/{subreddit}/about.json".format(subreddit)
	#Set a Custom User-Agent Header to avoid error
	headers = {'User-Agent': 'My_User_Agent'},
	 allow_redirects=False)
	#Set A Get Request to the Reddit API
	response = requests.get(url, headers=headers)
	#check the request
	if response.status_code == 200:
		#Parse The response of the JSON
		data = response.JSON()
		#Extract And Return
		return data['data']['subscribers']
	elif response.status_code == 404:
		#subreddit not found return 0
		return 0
