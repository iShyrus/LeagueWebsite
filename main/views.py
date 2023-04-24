from django.shortcuts import render
from django.http import HttpResponse
import league


# Create your views here.


def index(response):

    if 'message_frm' in response.POST:
        print("hi") 

    return render(response, "main/base.html",{})








def v1(request):

    a=35
    b=10
    result = a*b


    
    summonerName=request.GET.get('summonerName')
    print(summonerName)

    
    return render(request, "main/v1.html")





def summoner(request):

    name=request.GET.get('username')
    print(name)
    return render(request,
          "main/summoner.html")








def home(response):
    return render(response, "main/home.html",{})




def summonerName(response, summonerName, region):

    league.name = summonerName
    league.region = region


    league.runLeague()

    info ={
        'summonerName': summonerName,
        'region': region,
        'summonerLevel': league.summonerLevel,
        'summonerIcon': league.summonerIcon,

        'soloWins': league.soloDuoWins,
        'soloLosses': league.soloDuoLosses,
        'soloDuoWR': league.soloDuoWR,
        'soloDuoPoints': league.soloDuoPoints,
        'soloDuoRank': league.soloDuoRank,
        'soloDuoRankNumber': league.soloDuoRankNumber,

        'flexWins': league.flexWins,
        'flexLosses': league.flexLosses,
        'flexWR': league.flexWR,
        'flexPoints': league.flexPoints,
        'flexRank': league.flexRank,
        'flexRankNumber': league.flexRankNumber,
    }


    

    for i in range(len(league.summonerSpellName2)):
        summonerSpell = "summonerSpell" + str(i)
        info[summonerSpell] = league.summonerSpellName2[i]

        gameDuration = "gameDuration" + str(i)
        info[gameDuration] = league.gameDuration[i]
        
    for i in range(len(league.mostChampPlayed)):
        mostChampPlayed = 'mostChampPlayed' + str(i+1)
        info[mostChampPlayed] = league.mostChampPlayed[i]


    for i in range(len(league.winRecentGame)):
        gameWinLoss = "gameWinLoss" + str(i+1)
        info[gameWinLoss] = league.winRecentGame[i]

        mapsPlayed = "mapsPlayed" + str(i+1)
        info[mapsPlayed] = league.mapsPlayed[i]
        
        champPlayedInGame = "champPlayedInGame" + str(i+1)
        info[champPlayedInGame] = league.champPlayedInGame[i]

        totalMinions = "totalMinions " + str(i+1)
        info[totalMinions] = league.totalMinions[i]

    for i in range(len(league.kda)):
        kda = "kda"+ str(i+1)
        info[kda] = league.kda[i]


    for i in range(len(league.itemsBought)):
        itemsBought = "itemsBought" + str(i+1)
        info[itemsBought] = league.itemsBought[i]

    for i in range(len(league.playersInGame)):
        playersInGame = "playersInGame" + str(i+1)
        info[playersInGame] = league.playersInGame[i]

        allChampsPlayedInGame = "allChampsPlayedInGame" + str(i+1)
        info[allChampsPlayedInGame] = league.allChampsPlayedInGame[i]

    for i in range(len(league.top5ChampPlayedKDA)):
        top5KDA = "top5KDA" + str(i+1)
        info[top5KDA] = league.top5ChampPlayedKDA[i]
    
    return render(response,
          "main/summonerName.html", {'info':info},)
