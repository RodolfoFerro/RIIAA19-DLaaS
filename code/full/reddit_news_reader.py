# ===============================================================
# Author: Rodolfo Ferro
# Email: ferro@cimat.mx
# Twitter: @FerroRodolfo
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script was originally created by Rodolfo Ferro,
# for his workshop at RIIAA 2.0. Any explicit usage of
# this script or its contents is granted according to
# the license provided and its conditions.
# ===============================================================

# -*- coding: utf-8 -*-

from unidecode import unidecode
from pprint import pprint
import requests
import json


# Consume Reddit API:
def reddit_headlines(reddit):
    """Python function to get Reddit news."""

    # Set metadata to make request:
    url = "https://www.reddit.com/r/{}/.json?limit=10".format(reddit)
    headers = {'User-Agent': '{} Reddit headlines'.format(reddit)}

    # Consume Reddit's API to gather info:
    html = requests.get(url, headers=headers)

    # If status code is OK:
    if html.status_code == requests.codes.ok:
        # Parse resonse:
        info = json.loads(html.content.decode('utf-8'))
        # pprint(info)

        # Get relevant info:
        children = info['data']['children']
        titles = [unidecode(child['data']['title']) for child in children]
        titles = '... '.join(titles)
    else:
        titles = None

    return titles


if __name__ == "__main__":
    news = reddit_headlines('artificial')
    print(news)
