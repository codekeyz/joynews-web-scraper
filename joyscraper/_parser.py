import json

from bs4 import BeautifulSoup


def parse(resp, parser='html.parser'):
    return BeautifulSoup(resp, parser)


def tojson(data):
    return json.dumps(data)
