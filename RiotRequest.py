# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 17:54:43 2017

@author: lui
"""

from RiotAPI import RiotAPI

key = 'RGAPI-1d849512-91c5-4988-a8e4-48820ba41d3f'

listOfQKeys={'Ranked Solo/Duo Queue': 420, 'Ranked Flex Queue': 440, 'Normal Draft Pick': 400, 'Normal Blind Pick':430}

seasonList={'2014/2015': 7 , '2015/2016': 8 , '2016/2017': 9 , '2017/2018': 10}

def getSummonerAccountID(name, apiNumber):
    api = RiotAPI(apiNumber)
    rec = api.get_summoner_by_name(name)
    return rec

def getSummonerNamesOfMatch(accountID, apiNumber):
    api = RiotAPI(apiNumber)
    rec = api.get_summoner_of_match(accountID)
    return rec 

def getMatchlist(accountID, apiNumber):
    api = RiotAPI(apiNumber)
    rec = api.get_matchlist(accountID)
    return rec

def getSpecificMatchlist(accountID, apiNumber, QKey, Season=9):
    print(accountID, apiNumber, QKey, Season)
    api = RiotAPI(apiNumber)
    rec = api.get_specificMatchlist(accountID, Season, QKey)
    return rec


def getChampionName(championID, apiNumber):
    api = RiotAPI(apiNumber)
    rec = api.get_championName(championID)
    return rec

def sortMatchesToLane(matchList, parameter='Bottom'):
    positiveCriterium = []
    negativeCriterium = []
    counter = 0
    for element in matchList['matches']:
        counter = counter + 1
        if element['lane'] == 'BOTTOM':
            positiveCriterium = positiveCriterium + [element['gameId']]
        else:
            negativeCriterium = negativeCriterium + [element['gameId']]
        if len(positiveCriterium) > 300:
            return [positiveCriterium,negativeCriterium]
    return [positiveCriterium,negativeCriterium]


def sortMatchesByPartnerOld(matchList, Partner, apiNumber):
    api = RiotAPI(apiNumber)
    positiveCriterium = []
    negativeCriterium = []
    for number in matchList:
        names = api.get_summoner_of_match(number)
        flattenedNames = [value for sublist in names for value in sublist]
        if Partner in flattenedNames:
            positiveCriterium = positiveCriterium + [number]
        else:
            negativeCriterium = negativeCriterium + [number]
    return [positiveCriterium,negativeCriterium]

def sortMatchesByPartner(matchList, Partner, apiNumber): #assumes you don't have the matchInfo yet
    api = RiotAPI(apiNumber)
    positiveCriterium = []
    negativeCriterium = []
    for number in matchList:
        matchInfo = api.get_matchInfo(number)
        summonerNames = []
        for var in matchInfo['participantIdentities']:
            summonerNames = summonerNames + [var['player']['summonerName']]
        if Partner in summonerNames:
            positiveCriterium = positiveCriterium + [[number,matchInfo]]
        else:
            negativeCriterium = negativeCriterium + [[number,matchInfo]]
    return [positiveCriterium,negativeCriterium]

def sortMatchesByPartnerNoRate(matchList, Partner):
    positiveCriterium = []
    negativeCriterium = []
    for match in matchList:
        summonerNames=[]
        for variable in match[1]['participantIdentities']:
            print(variable)
            summonerNames = summonerNames + [variable['player']['summonerName']]
        if Partner in summonerNames:
            positiveCriterium = positiveCriterium + [match]
        else:
            negativeCriterium = negativeCriterium + [match]
    return [positiveCriterium,negativeCriterium]


def getGameInfos(matchList, apiNumber):
    api = RiotAPI(apiNumber)
    gameList=[]
    for number in matchList:
        matchInfo = api.get_matchInfo(number)
        gameList = gameList + [[number,matchInfo]]
    return gameList


def getMatchInfo(matchID, apiNumber):
    api = RiotAPI(apiNumber)
    rec = api.get_matchInfo(matchID)
    return rec

def checkWinOrLoose(PlayerName, MatchInfo):
    partId = 0
    for var in MatchInfo['participantIdentities']:
        if PlayerName == var['player']['summonerName']:
            partId = var['participantId']
        else:
            partId = partId
    if partId == 0:
        return('Error, Player not in Match')
    else:
        if partId < 6:
            return MatchInfo['teams'][0]['win']
        else:
            return MatchInfo['teams'][1]['win']
        
def calculateWinrate(listOfGames, PlayerName):
    counterGames = 0
    counterWins = 0
    counterLosses = 0
    for var in listOfGames:
        counterGames = counterGames + 1
        matchInfo = var[1]
        if checkWinOrLoose(PlayerName, matchInfo) == 'Win':
            counterWins = counterWins + 1
        else:
            counterLosses = counterLosses + 1
    if counterLosses + counterWins == counterGames:
        return counterWins/counterGames
    else:
        return 'error'
        
    
def fromMatchListGetMatchIds(matchList):
    ListWithIds = []
    for var in matchList:
        ListWithIds = ListWithIds + [var[0]]
    return ListWithIds

def extractMatchesWithAnotherPartner(matchList, AnotherPartner):
    positiveCriterium = []
    negativeCriterium = []
    for var in matchList:
        summonerNames = []
        for variable in var[1]['participantIdentities']:
            summonerNames = summonerNames + [variable['player']['summonerName']]
        if AnotherPartner in summonerNames:
            positiveCriterium = positiveCriterium + [var]
        else:
            negativeCriterium = negativeCriterium + [var]
    return [positiveCriterium ,negativeCriterium]

def findParticipantID(Playername, matchInfo):
    participantID = '0'
    for var in matchInfo['participantIdentities']:
        if var['player']['summonerName'] == Playername :
            participantID = var['participantId']
        else:
            participantID = participantID
    if participantID == 0:
        return 'error: Summoner not found. Check PlayerName'
    else:
        return participantID

def findPlayerStatsOfGame(PlayerName, matchInfo):
    participantID = findParticipantID(PlayerName, matchInfo)
    return matchInfo['participants'][int(participantID)-1]

def calculateCSDiffAverage(matchList, PlayerName):
    CSDiffEarly = 0
    CSDiffMiddle = 0
    gameCounter = 0
    foundGamesEarly = 0
    foundGamesMiddle = 0
    for var in matchList:
        gameCounter = gameCounter + 1
        stats = findPlayerStatsOfGame(PlayerName, var[1])
        if 'csDiffPerMinDeltas' in stats['timeline']:
            if '0-10' in stats['timeline']['csDiffPerMinDeltas']:
                CSDiffEarly = CSDiffEarly + stats['timeline']['csDiffPerMinDeltas']['0-10']
                foundGamesEarly = foundGamesEarly + 1
            if '10-20' in stats['timeline']['csDiffPerMinDeltas']:
                CSDiffMiddle = CSDiffEarly + stats['timeline']['csDiffPerMinDeltas']['10-20']
                foundGamesMiddle = foundGamesMiddle + 1
    CSDiffEarly = CSDiffEarly/foundGamesEarly
    CSDiffMiddle = CSDiffMiddle/foundGamesMiddle
    return [[foundGamesEarly,CSDiffEarly],[foundGamesMiddle,CSDiffMiddle]]

def calculateCSAverage(matchList, PlayerName):
    CSDiffEarly = 0
    CSDiffMiddle = 0
    gameCounter = 0
    foundGamesEarly = 0
    foundGamesMiddle = 0
    for var in matchList:
        gameCounter = gameCounter + 1
        stats = findPlayerStatsOfGame(PlayerName, var[1])
        if 'creepsPerMinDeltas' in stats['timeline']:
            if '0-10' in stats['timeline']['creepsPerMinDeltas']:
                CSDiffEarly = CSDiffEarly + stats['timeline']['creepsPerMinDeltas']['0-10']
                foundGamesEarly = foundGamesEarly + 1
            if '10-20' in stats['timeline']['creepsPerMinDeltas']:
                CSDiffMiddle = CSDiffEarly + stats['timeline']['creepsPerMinDeltas']['10-20']
                foundGamesMiddle = foundGamesMiddle + 1
    CSDiffEarly = CSDiffEarly/foundGamesEarly
    CSDiffMiddle = CSDiffMiddle/foundGamesMiddle
    return [[foundGamesEarly,CSDiffEarly],[foundGamesMiddle,CSDiffMiddle]] 

def divideMatchlistIntoPackages(matchList, packageSize):
    length = len(matchList)
    numberOfPackages = int(length/packageSize)  #omits last package with unfull size
    masterList = []
    for i in range(numberOfPackages):
        masterList = masterList + [[]]
    counter = 0
    listCounter = 0
    for element in matchList:
        counter = counter + 1
        if counter < packageSize + 1:
            masterList[listCounter] = masterList[listCounter] + [matchList[-(counter + packageSize*listCounter)]]
        else:
            counter = 0
            listCounter = listCounter + 1
        if listCounter >= numberOfPackages:
            return masterList
    return masterList

def createList(number):
    bigList = []
    i = 0
    while i<number:
        bigList = bigList + [[i,i]]
        i = i+1
    return bigList


#def calculatecsDevelpoment(matchList, PlayerName):
    
          


if __name__== "__main__":
    bigList = createList(90)
    print(bigList)
    print(divideMatchlistIntoPackages(bigList,20))
    
#    personalData = getSummonerAccountID('Stringtheorie', key)
#    print(personalData)
#    ID = personalData['accountId']
#    matchList = getSpecificMatchlist(ID, key, 440,9)
#    BottomLaneMatches=sortMatchesToLane(matchList)
#    print(BottomLaneMatches)
#    print(BottomLaneMatches)
#    DuoList = sortMatchesByPartner(BottomLaneMatches[0], 'jackreacher133', key)
#    MatchesWithAdam = DuoList[0]
#    print(MatchesWithAdam)
#    MatchesWithoutAdam = DuoList[1]
#    List = extractMatchesWithAnotherPartner(MatchesWithAdam, 'Gololol')
#    MatchesWithAdamAndGololol = List[0]
#    MatchesWithAdamWithoutGololol = List[1]
#    winrate = calculateWinrate(MatchesWithAdamAndGololol, 'Stringtheorie')
#    print(winrate)
#    winrate2 = calculateWinrate(MatchesWithAdamWithoutGololol, 'Stringtheorie')
#    print(winrate2)
#    print(calculateWinrate(MatchesWithoutAdam, 'Stringtheorie'))
#    print(calculateCSDiffAverage(MatchesWithAdamWithoutGololol, 'Stringtheorie'))
#    print(calculateCSAverage(MatchesWithAdamWithoutGololol, 'Stringtheorie'))
#    print(calculateCSDiffAverage(MatchesWithAdamAndGololol, 'Stringtheorie'))
#    print(calculateCSAverage(MatchesWithAdamAndGololol, 'Stringtheorie'))
#    gameInfo = getGameInfos(BottomLaneMatches[0], key)
#    print(gameInfo)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    