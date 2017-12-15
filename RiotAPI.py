# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 17:30:00 2017

@author: lui
"""

import requests as rq

import RiotConstants as Consts

class RiotAPI(object):
    
    def __init__(self, api_key, region=Consts.REGIONS['europe_west']):
        self.api_key = api_key
        self.region = region
        
    def _request(self, api_url, params={}):
        args = {'api_key': self.api_key}
        response = rq.get(Consts.URL['base'].format(proxy=self.region,region=self.region,url=api_url))
        return response.json()
        
    def get_summoner_by_name(self,name):
        api_url = Consts.URL['summoner_by_name'].format(version=Consts.API_VERSIONS['summoner'], accountId=name, apikey=self.api_key)
        return self._request(api_url)
    
    def get_summoner_of_match(self,MatchID):
        api_url = Consts.URL['match'].format(version=Consts.API_VERSIONS['summoner'], matchId=MatchID, apikey=self.api_key)
        response = self._request(api_url)
        team1 = []
        team2 = []
        for var in response['participantIdentities']:
            if var['participantId'] < 6:
                team1 = team1 + [var['player']['summonerName']]
            else:
                team2 = team2 + [var['player']['summonerName']]
        return [team1,team2]
        
    def get_matchlist(self,AccountID):
        api_url = Consts.URL['matchlist'].format(version=Consts.API_VERSIONS['summoner'], accountId=AccountID, apikey=self.api_key)
        return self._request(api_url)
    
    def get_matchlistrecent(self, AccountID):
        api_url = Consts.URL['matchlistrecent'].format(version=Consts.API_VERSIONS['summoner'], accountId=AccountID, apikey=self.api_key)
        return self._request(api_url)
    
    def get_specificMatchlist(self, AccountID, Season, QKey):
        api_url = Consts.URL['matchlistWithParams'].format(version=Consts.API_VERSIONS['summoner'], accountId=AccountID, SEASON=Season, QKEY=QKey, apikey=self.api_key) 
        return self._request(api_url)
                            
    def get_championName(self, championID):
        api_url = Consts.URL['championName'].format(version=Consts.API_VERSIONS['summoner'], champId=championID, apikey=self.api_key)
        return self._request(api_url)
    
    def get_championStatus(self, championID):
        api_url = Consts.URL['championStatus'].format(version=Consts.API_VERSIONS['summoner'], champId=championID, apikey=self.api_key)
        return self._request(api_url)
    
    def get_matchInfo(self, MatchID):
        api_url = Consts.URL['match'].format(version=Consts.API_VERSIONS['summoner'], matchId=MatchID, apikey=self.api_key)
        response = self._request(api_url)
        return response
    
        
