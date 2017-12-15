# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 17:17:22 2017

@author: lui
"""

URL = {
    'base': 'https://{region}.api.riotgames.com{url}',
    'summoner_by_name': '/lol/summoner/v{version}/summoners/by-name/{accountId}?api_key={apikey}',
    'match': '/lol/match/v{version}/matches/{matchId}?api_key={apikey}',
    'matchlist': '/lol/match/v{version}/matchlists/by-account/{accountId}?api_key={apikey}',
    'matchlistrecent': '/lol/match/v{version}/matchlists/by-account/{accountId}/recent?api_key={apikey}',
    'championStatus': '/lol/platform/v{version}/champions/{champId}?api_key={apikey}',
    'championName': '/lol/static-data/v3/champions/{champId}?api_key={apikey}',
    'matchlistWithParams': '/lol/match/v{version}/matchlists/by-account/{accountId}?queue={QKEY}&season={SEASON}&api_key={apikey}'
}

API_VERSIONS = {
    'summoner': '3'
}

REGIONS = {
    'europe_west': 'euw1',
    'north_america': 'na1'
}

