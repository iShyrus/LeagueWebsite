import random
import requests
import json
import os
from pprint import pprint
import csv
import time



def runLeague():
    #test

    global region,top5ChampPlayedKDA,allChampsPlayedInGame, playersInGame, itemsBought, totalMinions,kda, gameDuration, summonerSpellName2,summonerSpellName, name, winRecentGame, soloDuoWins, soloDuoLosses, soloDuoWR, soloDuoPoints, soloDuoRank, soloDuoRankNumber, flexWins, flexLosses, flexWR, flexPoints, flexRank, flexRankNumber, summonerLevel, summonerIcon, mostChampPlayed, mapsPlayed,champPlayedInGame
    

    

    soloDuoWins = 0
    soloDuoLosses = 0
    soloDuoWR = 0
    soloDuoPoints = 0
    soloDuoRank = "UNRANKED"
    soloDuoRankNumber = 0
    unknownVariable = "charlesWasHere"
    
    flexWins = 0
    flexLosses = 0
    flexWR = 0
    flexPoints = 0
    flexRank = "UNRANKED"
    flexRankNumber = 0

    if region == "NA":
        region ="na1"
        region1 ="americas"
    elif region =="BR":
        region="br1"
        region1 ="americas"
    elif region =="EUN":
        region="eun1"
        region1 ="europe"
    elif region =="EUW":
        region="euw1"
        region1 ="europe" 
    elif region =="JP":
        region="jp1"
        region1 ="asia"     
    elif region =="KR":
        region="kr"
        region1 ="asia" 
    elif region =="LAN":
        region="la1"
        region1 ="americas" 
    elif region =="LAS":
        region="la2"
        region1 ="americas" 
    elif region =="OCE":
        region="oc1"
        region1 ="asia" 
    elif region =="TR":
        region="tr1"
        region1 ="asia" 
    elif region =="RU":
        region="ru"
        region1 ="asia" 



    apikey= ("RGAPI-2b8c2d30-7af6-45dc-9109-f64a6c478fb0")  
    r = requests.get("https://"+region+".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name +"?api_key="+apikey).json()
    encryptedSummonerID = r['id']
    leagueRank = requests.get("https://"+region+".api.riotgames.com/lol/league/v4/entries/by-summoner/"+encryptedSummonerID+"?api_key=RGAPI-2b8c2d30-7af6-45dc-9109-f64a6c478fb0").json()
    puuID=r['puuid']

    #pprint(r)
    #print(puuID)
    #pprint(leagueRank)



#--------------------------------------------------------------------- SUMMONER LEVEL / ICON

    summonerReq = requests.get("https://"+region+".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + apikey).json()

    summonerLevel = summonerReq['summonerLevel']
    summonerIcon = summonerReq['profileIconId']

#--------------------------------------------------------------------- LEAGUE RANKS
    size = len(leagueRank)
    #pprint(leagueRank)
    for i in range(size):

        losses = int(leagueRank[i]['losses'])
        wins = int(leagueRank[i]['wins'])
        wr=float(wins/(wins+losses))*100
        queueType = str(leagueRank[i]['queueType'])
        leaguePoints = int(leagueRank[i]['leaguePoints'])


        

        if(queueType=='RANKED_FLEX_SR'):
            rank = leagueRank[i]['tier']
            rankNumber = leagueRank[i]['rank']
            queueType="Ranked Flex"
            flexWins = wins
            flexLosses = losses
            flexWR = "{:.2f}".format(wr)
            flexPoints = leaguePoints
            flexRank = rank
            flexRankNumber = rankNumber

        elif(queueType=='RANKED_SOLO_5x5') :
            rank = leagueRank[i]['tier']
            rankNumber = leagueRank[i]['rank']
            queueType= "Ranked Solo/Duo"
            soloDuoWins = wins
            soloDuoLosses = losses
            soloDuoWR = "{:.2f}".format(wr)
            soloDuoPoints = leaguePoints
            soloDuoRank = rank
            soloDuoRankNumber = rankNumber

        print("Queue Type: "+queueType)
        print("Wins: {}".format(wins))
        print("Losses: {}".format(losses))
        print("Win Rate: {}%\n".format(wr))



    #pprint(leagueRank)


    #w = int(2)
    #w1 = int(3)
    #print("PP {}{}".format(w,w1))


    #___________________________________________________________________________________________________________

    matchHistory = requests.get("https://"+region1+".api.riotgames.com/lol/match/v5/matches/by-puuid/"+puuID+"/ids?start=0&count=100&api_key=RGAPI-2b8c2d30-7af6-45dc-9109-f64a6c478fb0").json()

    print(puuID)

    f = open('queues.json')
    matchDataType = json.load(f)
    summonerChampWR={}
    summonerChampPlayed={}
    championKills = {}
    championDeaths = {}
    championAssists = {}
    mapsPlayed = []
    champPlayedInGame = []
    winRecentGame = []
    summonerSpell = []
    gameDuration = []
    kda = []
    totalMinions = []
    itemsBought = []
    playersInGame = []
    allChampsPlayedInGame = []
    top5ChampPlayedKDA = []
    killedMinionsAverage = {}
    top5ChampsMinutes = {}
    top5ChampsWin = {}




    start = time.time()


    for i in range(30):
        matchHistory1= matchHistory[i]
        matchDetail1 = requests.get("https://"+region1+".api.riotgames.com/lol/match/v5/matches/"+matchHistory1+"?api_key=RGAPI-2b8c2d30-7af6-45dc-9109-f64a6c478fb0").json()

        gameDurationMin = str(int(matchDetail1['info']['gameDuration']/60)) +"min"
        gameDurationSec = str(int(matchDetail1['info']['gameDuration']%60)) +"s"
        gameDuration.append(gameDurationMin)
        gameDuration.append(gameDurationSec)


        matchType = int(matchDetail1['info']['queueId'])
        #print("Last Match:\n")  
        
        


        for i in range(len(matchDataType)):
            if matchType==matchDataType[i]['queueId']:

                #print(matchType)
                #print(matchDataType[i]['map'])
                #print(matchDataType[i]['description'])

                if( matchDataType[i]['description'] =="5v5 Draft Pick games"):
                    mapsPlayed.append("Draft Pick")
                elif( matchDataType[i]['description'] =="5v5 Blind Pick games"):
                    mapsPlayed.append("Blind Pick")
                elif( matchDataType[i]['description'] =="5v5 ARAM games"):
                    mapsPlayed.append("ARAM")
                elif( matchDataType[i]['description'] =="5v5 Ranked Solo games"):
                    mapsPlayed.append("Ranked Solo")
                elif( matchDataType[i]['description'] =="5v5 Ranked Flex games"):
                    mapsPlayed.append("Ranked Flex")
                elif( matchDataType[i]['description'] =="Clash games"):
                    mapsPlayed.append("Clash")
                else:
                    mapsPlayed.append("Unknown")

                #print("\n")





        for i in range(10):
            #print(matchDetail1['info']['participants'][i]['lane'],matchDetail1['info']['participants'][i]['championName'], " - ",matchDetail1['info']['participants'][i]['summonerName'])
            playersInGame.append(matchDetail1['info']['participants'][i]['summonerName'])

            allChampsPlayedInGame.append(matchDetail1['info']['participants'][i]['championName'])


            if(matchDetail1['info']['participants'][i]['summonerName']==name):


                if matchDetail1['info']['participants'][i]['championName'] in championKills:
                    championKills[matchDetail1['info']['participants'][i]['championName']] += matchDetail1['info']['participants'][i]['kills']
                else:
                    championKills[matchDetail1['info']['participants'][i]['championName']] = matchDetail1['info']['participants'][i]['kills']

                if matchDetail1['info']['participants'][i]['championName'] in championDeaths:
                    championDeaths[matchDetail1['info']['participants'][i]['championName']] += matchDetail1['info']['participants'][i]['deaths']
                else:
                    championDeaths[matchDetail1['info']['participants'][i]['championName']] = matchDetail1['info']['participants'][i]['deaths']
                    
                if matchDetail1['info']['participants'][i]['championName'] in championAssists:
                    championAssists[matchDetail1['info']['participants'][i]['championName']] += matchDetail1['info']['participants'][i]['assists']
                else:
                    championAssists[matchDetail1['info']['participants'][i]['championName']] = matchDetail1['info']['participants'][i]['assists']  

                if matchDetail1['info']['participants'][i]['championName'] in killedMinionsAverage:
                    killedMinionsAverage[matchDetail1['info']['participants'][i]['championName']] += matchDetail1['info']['participants'][i]['neutralMinionsKilled'] + matchDetail1['info']['participants'][i]['totalMinionsKilled']
                else:
                    killedMinionsAverage[matchDetail1['info']['participants'][i]['championName']] = matchDetail1['info']['participants'][i]['neutralMinionsKilled'] + matchDetail1['info']['participants'][i]['totalMinionsKilled']


                if matchDetail1['info']['participants'][i]['championName'] in top5ChampsMinutes:
                    top5ChampsMinutes[matchDetail1['info']['participants'][i]['championName']] += matchDetail1['info']['gameDuration']
                else:
                    top5ChampsMinutes[matchDetail1['info']['participants'][i]['championName']] = matchDetail1['info']['gameDuration']

                if matchDetail1['info']['participants'][i]['win'] == True:
                    if matchDetail1['info']['participants'][i]['championName'] in top5ChampsWin:
                        top5ChampsWin[matchDetail1['info']['participants'][i]['championName']] += 1
                    else:
                        top5ChampsWin[matchDetail1['info']['participants'][i]['championName']] = 1


                champPlayedInGame.append(matchDetail1['info']['participants'][i]['championName'])
                #print(matchDetail['info']['participants'][i]['championName'],matchDetail['info']['participants'][i]['win'])

                kda.append(matchDetail1['info']['participants'][i]['kills'])
                kda.append(matchDetail1['info']['participants'][i]['deaths'])
                kda.append(matchDetail1['info']['participants'][i]['assists'])

                totalMinions.append(matchDetail1['info']['participants'][i]['totalMinionsKilled'] + matchDetail1['info']['participants'][i]['neutralMinionsKilled'])

                summonerSpell.append(matchDetail1['info']['participants'][i]['summoner1Id'])
                summonerSpell.append(matchDetail1['info']['participants'][i]['summoner2Id'])

                itemsBought.append(matchDetail1['info']['participants'][i]['item0'])
                itemsBought.append(matchDetail1['info']['participants'][i]['item1'])
                itemsBought.append(matchDetail1['info']['participants'][i]['item2'])
                itemsBought.append(matchDetail1['info']['participants'][i]['item3'])
                itemsBought.append(matchDetail1['info']['participants'][i]['item4'])
                itemsBought.append(matchDetail1['info']['participants'][i]['item5'])
                itemsBought.append(matchDetail1['info']['participants'][i]['item6'])



                if (matchDetail1['info']['participants'][i]['win'] ==True):
                    winRecentGame.append("Victory")
                else:
                    winRecentGame.append("Defeat")

                    #print(matchDetail1['info']['participants'][i]['win'])



                if matchDetail1['info']['participants'][i]['championName'] in summonerChampWR:
                    summonerChampWR[matchDetail1['info']['participants'][i]['championName']] += 1
                    summonerChampPlayed[matchDetail1['info']['participants'][i]['championName']] += 1
                    if matchDetail1['info']['participants'][i]['win'] == True:
                        summonerChampWR[matchDetail1['info']['participants'][i]['championName']+"WR"] += 1                

                else:
                    summonerChampWR[matchDetail1['info']['participants'][i]['championName']] = 1
                    summonerChampPlayed[matchDetail1['info']['participants'][i]['championName']] = 1
                    if matchDetail1['info']['participants'][i]['win'] == True:
                        summonerChampWR[matchDetail1['info']['participants'][i]['championName']+"WR"] = 1
                    else:
                        summonerChampWR[matchDetail1['info']['participants'][i]['championName']+"WR"] = 0




            

                        



    end = time.time()
    print(end - start)
    start = time.time()


            #if i == 4:
                #print("\n")

        #print("\nGame Duration: {}".format(gameDuration))

        #print("__________________________________________________________________________")


    f.close()


    count=0

    #print(count)




    #print(summonerChampWR)
    #print(summonerChampPlayed)
    
    mostChampPlayed = sorted(summonerChampPlayed, key=summonerChampPlayed.get, reverse=True)[:100]


    #print(unknownVariable)




    
    summonerSpellName2 = []

    s2 = open('summonerSpells2.json')
    summonerSpells2JSON = json.load(s2)
    #pprint(summonerSpells2JSON[1])

    for i in range(len(summonerSpell)):
        summonerSpellID = summonerSpell[i]
        for i in range(len(summonerSpells2JSON)):
            if (summonerSpellID == int(summonerSpells2JSON[i]['key'])):

                summonerSpellName2.append(summonerSpells2JSON[i]['id'])

    #pprint(summonerSpellName2)
    
    #print(winRecentGame)

    #print(championKills)
    #print(championDeaths)
    #print(championAssists)
    #print(mostChampPlayed)
    #print(killedMinionsAverage)
    #print (top5ChampsWin)

    for i in range(5):
        top5ChampPlayedKDA.append(summonerChampPlayed.get(mostChampPlayed[i]))
        top5ChampPlayedKDA.append(championKills.get(mostChampPlayed[i]))
        top5ChampPlayedKDA.append(championDeaths.get(mostChampPlayed[i]))
        top5ChampPlayedKDA.append(championAssists.get(mostChampPlayed[i]))
        top5ChampPlayedKDA.append(killedMinionsAverage.get(mostChampPlayed[i]))
        top5ChampPlayedKDA.append(top5ChampsMinutes.get(mostChampPlayed[i]))
        top5ChampPlayedKDA.append(top5ChampsWin.get(mostChampPlayed[i]))

    end = time.time()

    print(start-end)



    #print(top5ChampPlayedKDA)


#name = "Dyrus"
#runLeague()





