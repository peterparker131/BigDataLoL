#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 12:45:15 2017

@author: lui
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 11:49:06 2017

@author: lui
"""

import tkinter as tk

import RiotRequest as rr

from PIL import Image, ImageTk


largeFont = ('Verdana', 14)

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)   #open a tkinter window
        self.geometry('1066x600')
        
#        self.winrate=tk.DoubleVar()
        
        container = tk.Frame(self)              #pick a frame containing all windows 
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {}
        
        for F in (startPage, findGames, apiQuestion, findLane, calculate):
            frame = F(container, self)        
            self.frames[F] = frame       
            frame.grid(row=0, column=0, sticky='nsew')
        
        self.showFrame(startPage)
#        
    def showFrame(self, cont):
         frame = self.frames[cont]
         frame.tkraise()
         
    def close(self):
        self.root.destroy()
        
    def addFrame(self, name):
        container = tk.Frame(self)              #pick a frame containing all windows 
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        frame = name(container, self)
        self.frames[name] = frame
        frame.grid(row=0, column=0, sticky='nsew')
         
class DataApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)   #open a tkinter window
        self.geometry('1066x600')
        
        container = tk.Frame(self)              #pick a frame containing all windows 
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {}
        
        for F in (startPage, findGames, apiQuestion, findLane, calculate, conclusion, addPartner):
            frame = F(container, self)        
            self.frames[F] = frame       
            frame.grid(row=0, column=0, sticky='nsew')
        
        self.showFrame(conclusion)
#        
    def showFrame(self, cont):
         frame = self.frames[cont]
         frame.tkraise()
         
class DataApp2(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)   #open a tkinter window
        self.geometry('1066x600')
        
        container = tk.Frame(self)              #pick a frame containing all windows 
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {}
        
        for F in (startPage, findGames, apiQuestion, findLane, calculate, conclusion, addPartner, conclusionWithPartner):
            frame = F(container, self)        
            self.frames[F] = frame       
            frame.grid(row=0, column=0, sticky='nsew')
        
        self.showFrame(conclusionWithPartner)
#        
    def showFrame(self, cont):
         frame = self.frames[cont]
         frame.tkraise()
        
        
class startPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        load = Image.open('Teemo3.png')
        render = ImageTk.PhotoImage(load, size=0.3)
        
        label2 = tk.Label(self, image=render)
        label2.image = render
        label2.place(x=0, y=0, relwidth=1, relheight=1)
        
        label = tk.Label(self, text="Start Page", font=largeFont)                         
        label.pack(pady=10,padx=10)
        button = tk.Button(self, text="Start",
                           command=lambda: controller.showFrame(apiQuestion))
        button.pack()

class apiQuestion(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        load = Image.open('Poros2.jpg')
        render = ImageTk.PhotoImage(load, size=0.3)
        
        label2 = tk.Label(self, image=render)
        label2.image = render
        label2.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.controller=controller
        self.apiKey = tk.StringVar() 
        
        label = tk.Label(self, text="API Key", font=largeFont)
        label.pack(pady=10,padx=10)
        
        entry = tk.Entry(self, textvariable=self.apiKey, width=50)
        entry.pack()
        
        button1 = tk.Button(self, text="Back to Start",
                            command=lambda: controller.showFrame(startPage))
        button1.pack()
        
        button2 = tk.Button(self, text="Continue",
                            command=lambda: mergeFunction(getApi, findGames, self.controller, self.apiKey))
        button2.pack()
        
        button3 = tk.Button(self, text="Back",
                            command=lambda: controller.showFrame(startPage))
        button3.pack()
        
        
class findGames(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        labelMain = tk.Label(self, text="Find Games", font=largeFont)
        labelMain.pack(pady=10,padx=10)
        
        load = Image.open('Poros2.jpg')
        render = ImageTk.PhotoImage(load, size=0.3)
        
        label2 = tk.Label(self, image=render)
        label2.image = render
        label2.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.controller = controller
        self.gameMode = tk.StringVar()
        self.summonerName = tk.StringVar()
        self.season = tk.StringVar()
        
        labelSummonerName = tk.Label(self, text="Please enter your summoner name:")
        labelSummonerName.pack()
        entrySummonerName = tk.Entry(self, textvariable=self.summonerName, width=30)
        entrySummonerName.pack()
        
        labelGameMode = tk.Label(self, text="Please enter a game Mode from the following List:")
        labelGameMode.pack()
        
        radioGameMode1 = tk.Radiobutton(self, text="Ranked Solo/Duo Queue", variable=self.gameMode, value="Ranked Solo/Duo Queue").pack()
        radioGameMode1 = tk.Radiobutton(self, text="Ranked Flex Queue", variable=self.gameMode, value= "Ranked Flex Queue").pack()
        radioGameMode1 = tk.Radiobutton(self, text="Normal Blind Pick", variable=self.gameMode, value="Normal Blind Pick").pack()
        radioGameMode1 = tk.Radiobutton(self, text="Normal Draft Pick", variable=self.gameMode, value="Normal Draft Pick").pack()
        
        labelSeason = tk.Label(self, text="Please enter a season. The following Seasons are available:")
        labelSeason.pack()
        
        radioSeason1 = tk.Radiobutton(self, text="2014/2015", variable=self.season, value="2014/2015").pack()
        radioSeason1 = tk.Radiobutton(self, text="2015/2016", variable=self.season, value= "2015/2016").pack()
        radioSeason1 = tk.Radiobutton(self, text="2016/2017", variable=self.season, value="2016/2017").pack()
        radioSeason1 = tk.Radiobutton(self, text="2017/2018", variable=self.season, value="2017/2018").pack()

        button1 = tk.Button(self, text="Back to Start",
                            command=lambda: controller.showFrame(startPage))
        button1.pack()
               
        button2 = tk.Button(self, text="Continue",
                            command=lambda: merge3Functions(getMode, getSummonerName, getSeason, findLane, self.controller, self.gameMode, self.summonerName, self.season))
        button2.pack()
        
        button3 = tk.Button(self, text="Back",
                            command=lambda: controller.showFrame(apiQuestion))
        button3.pack()
        
class findLane(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        labelMain = tk.Label(self, text="Find Games", font=largeFont)
        labelMain.pack(pady=10,padx=10)
        
        load = Image.open('Poros2.jpg')
        render = ImageTk.PhotoImage(load, size=0.3)
        
        label2 = tk.Label(self, image=render)
        label2.image = render
        label2.place(x=0, y=0, relwidth=1, relheight=1)
     
        self.controller = controller
        self.Lane = tk.StringVar()
        
        labelstartingLane = tk.Label(self, text="Please enter a starting Lane from the following List")
        labelstartingLane.pack()
        
        radioLane = tk.Radiobutton(self, text="Bottom", variable=self.Lane, value="Bottom").pack()
        radioLane = tk.Radiobutton(self, text="Top", variable=self.Lane, value= "Top").pack()
        radioLane = tk.Radiobutton(self, text="Jungle", variable=self.Lane, value="Jungle").pack()
        radioLane = tk.Radiobutton(self, text="Mid", variable=self.Lane, value="Mid").pack()
        
        button1 = tk.Button(self, text="Back to Start",
                            command=lambda: controller.showFrame(startPage))
        button1.pack()
               
        button2 = tk.Button(self, text="Continue",
                            command=lambda: mergeFunction(getLane, calculate, self.controller, self.Lane))
        button2.pack()
        
        button3 = tk.Button(self, text="Back",
                            command=lambda: controller.showFrame(findGames))
        button3.pack()
        
class calculate(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        labelMain = tk.Label(self, text="Find Games", font=largeFont)
        labelMain.pack(pady=10,padx=10)
        self.controller = controller
        
        load = Image.open('Poros2.jpg')
        render = ImageTk.PhotoImage(load, size=0.3)
        
        label2 = tk.Label(self, image=render)
        label2.image = render
        label2.place(x=0, y=0, relwidth=1, relheight=1)
        
        global summonerName
        global api
        global season
        global mode
        global lane

        button1 = tk.Button(self, text="Back to Start",
                            command=lambda: controller.showFrame(startPage))
        button1.pack()
               
        button2 = tk.Button(self, text="Calculate Stats",
                            command=lambda: mergeGameList(findGameList, conclusion, self.controller, summonerName, api, lane, mode, season))
        button2.pack()
        
        button3 = tk.Button(self, text="Back",
                            command=lambda: controller.showFrame(findLane))
        button3.pack()

        
class conclusion(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        labelMain = tk.Label(self, text="Conclusion", font=largeFont)
        labelMain.pack(pady=10,padx=10)
        self.controller = controller
        
        load = Image.open('Poros2.jpg')
        render = ImageTk.PhotoImage(load, size=0.3)
        
        label2 = tk.Label(self, image=render)
        label2.image = render
        label2.place(x=0, y=0, relwidth=1, relheight=1)
        
        labelDescription = tk.Label(self, text="The following Data could be analyzed:")
        labelDescription.pack()
        
        global winrate
        global csDiff
        global csAverage
        global csDiffAt10
        global csDiffAt20
        global csAt10
        global csAt20
        global Games
        
        labelMain = tk.Label(self, text="We analyzed  " + str(len(Games)) + " games")
        labelMain.pack()
        labelWinrate = tk.Label(self, text=' Your winrate is :' + str(winrate))
        labelWinrate.pack()
        labelcsDiffAt10 = tk.Label(self, text=('CS Difference at 10 min:' + str(csDiffAt10)))
        labelcsDiffAt10.pack()
        labelcsDiffAt20 = tk.Label(self, text='CS Difference at 20 min:' + str(csDiffAt20))
        labelcsDiffAt20.pack()
        
        button1 = tk.Button(self, text="Analyze these Matches by Partner",
                            command=lambda: controller.showFrame(addPartner))
        button1.pack()
        
        button1 = tk.Button(self, text="Quit",
                            command=lambda: controller.destroy())
        button1.pack()
        
class addPartner(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        labelMain = tk.Label(self, text="Find Games", font=largeFont)
        labelMain.pack(pady=10,padx=10)
        self.controller = controller
        self.partner = tk.StringVar()
        
        load = Image.open('Poros2.jpg')
        render = ImageTk.PhotoImage(load, size=0.3)
        
        label2 = tk.Label(self, image=render)
        label2.image = render
        label2.place(x=0, y=0, relwidth=1, relheight=1)
        
        labelPartner = tk.Label(self, text="Enter the summoner Name of your Partner")
        labelPartner.pack()
        
        entryPartner = tk.Entry(self, textvariable=self.partner, width=30)
        entryPartner.pack()
               
        button2 = tk.Button(self, text="Calculate Stats",
                            command=lambda: mergeGameListWithPartner(findGameListWithPartner, conclusion, self.controller, self.partner.get(), summonerName))
        button2.pack()
        
        button3 = tk.Button(self, text="Back",
                            command=lambda: controller.showFrame(conclusion))
        button3.pack()
        
class conclusionWithPartner(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        labelMain = tk.Label(self, text="Conclusion", font=largeFont)
        labelMain.pack(pady=10,padx=10)
        self.controller = controller
        
        load = Image.open('Poros2.jpg')
        render = ImageTk.PhotoImage(load, size=0.3)
        
        label2 = tk.Label(self, image=render)
        label2.image = render
        label2.place(x=0, y=0, relwidth=1, relheight=1)
        
        labelDescription = tk.Label(self, text="The following Data could be analyzed:")
        labelDescription.pack()
        
        global partner
        
        global winrateWithPartner
        global csDiffWithPartner
        global csAverageWithPartner
        global csDiffAt10WithPartner
        global csDiffAt20WithPartner
        global csAt10WithPartner
        global csAt20WithPartner
        global gamesWithPartner
        
        global winrateWithoutPartner
        global csDiffWithoutPartner
        global csAverageWithoutPartner
        global csDiffAt10WithoutPartner
        global csDiffAt20WithoutPartner
        global csAt10WithoutPartner
        global csAt20WithoutPartner
        global gamesWithoutPartner
        
        labelMainWithPartner = tk.Label(self, text="We analyzed  " + str(gamesWithPartner) + " games with " + partner + ":")
        labelMainWithPartner.pack()
        labelWinrateWithPartner = tk.Label(self, text=' Your winrate is :' + str(winrateWithPartner))
        labelWinrateWithPartner.pack()
        labelcsDiffAt10WithPartner = tk.Label(self, text=('CS Difference at 10 min:' + str(csDiffAt10WithPartner)))
        labelcsDiffAt10WithPartner.pack()
        labelcsDiffAt20WithPartner = tk.Label(self, text='CS Difference at 20 min:' + str(csDiffAt20WithPartner))
        labelcsDiffAt20WithPartner.pack()
        
        labelSpace =tk.Label(self, text='     ')
        labelSpace.pack()
        
        labelMainWithoutPartner = tk.Label(self, text="We analyzed  " + str(gamesWithoutPartner) + " games without " + partner + ":")
        labelMainWithoutPartner.pack()
        labelWinrateWithoutPartner = tk.Label(self, text=' Your winrate is :' + str(winrateWithoutPartner))
        labelWinrateWithoutPartner.pack()
        labelcsDiffAt10WithoutPartner = tk.Label(self, text=('CS Difference at 10 min:' + str(csDiffAt10WithoutPartner)))
        labelcsDiffAt10WithoutPartner.pack()
        labelcsDiffAt20WithoutPartner = tk.Label(self, text='CS Difference at 20 min:' + str(csDiffAt20WithoutPartner))
        labelcsDiffAt20WithoutPartner.pack()
        
        button1 = tk.Button(self, text="Quit",
                            command=lambda: controller.destroy())
        button1.pack()
    
    
def getApi(name):
    global api
    var=name.get()
    api = var   
    
def getMode(name):
    global mode
    var=name.get()
    mode = var  
    
def getLane(name):
    global lane
    var=name.get()
    lane = var  
    
def getSummonerName(name):
    global summonerName
    var=name.get()
    summonerName = var 
    
def getSeason(name):
    global season
    var=name.get()
    season = var 
    
def mergeFunction(f, window, controller, argument1):
    f(argument1)
    controller.showFrame(window)
    
def merge2Functions(f, g, window, controller, argument1, argument2):
    f(argument1)
    g(argument2)
    controller.showFrame(window)
    
def merge3Functions(f, g, h, window, controller, argument1, argument2, argument3):
    f(argument1)
    g(argument2)
    h(argument3)
    controller.showFrame(window)
    
def mergeGameList(f, window, controller, argument1, argument2, argument3, argument4, argument5):
    f(argument1,  argument2, argument3, argument4, argument5, controller)
    controller.addFrame(window)
    controller.showFrame(window)
#    controller.destroy()
    
def mergeGameListWithPartner(f, window, controller, argument1, argument2):
    f(argument1,  argument2)
#    controller.showFrame(window)
    controller.destroy()
      
def findGameList(summonerName, key, lane, queue, season, controller):
    seasonNumber = rr.seasonList[season]
    personalData = rr.getSummonerAccountID(summonerName, key)
    print(personalData)
    summonerID = personalData['accountId']
    matchList = rr.getSpecificMatchlist(summonerID, key, rr.listOfQKeys[queue] , seasonNumber)
    matchesByLane = rr.sortMatchesToLane(matchList, 'lane')
    gameInfo = rr.getGameInfos(matchesByLane[0], key)
    global Games
    Games = gameInfo
    global winrate
    global csDiff
    global csAverage
    global csDiffAt10
    global csDiffAt20
    global csAt10
    global csAt20
    number = rr.calculateWinrate(gameInfo, summonerName)
    winrate  = number
    csDiff = rr.calculateCSDiffAverage(gameInfo, summonerName)
    csAverage = rr.calculateCSAverage(gameInfo, summonerName)
    csDiffAt10 = csDiff[0][1]*10
    csDiffAt20 = csDiff[1][1]*10 + csDiffAt10
    csAt10 = csAverage[0][1]*10
    csAt20 = csAverage[1][1]*10 + csAt10    
    
def findGameListWithPartner(Partner, summonerName):
    global partner
    partner = Partner
    global Games
    sortedMatches = rr.extractMatchesWithAnotherPartner(Games, Partner)
    global winrateWithPartner
    global csDiffWithPartner
    global csAverageWithPartner
    global csDiffAt10WithPartner
    global csDiffAt20WithPartner
    global csAt10WithPartner
    global csAt20WithPartner
    global gamesWithPartner
    if len(sortedMatches[0])==0:
        gamesWithPartner=0
    else:
        gamesWithPartner = len(sortedMatches[0])
        winrateWithPartner = rr.calculateWinrate(sortedMatches[0], summonerName)
        csDiffWithPartner = rr.calculateCSDiffAverage(sortedMatches[0], summonerName)
        csAverageWithPartner = rr.calculateCSAverage(sortedMatches[0], summonerName)
        csDiffAt10WithPartner = csDiffWithPartner[0][1]*10
        csDiffAt20WithPartner = csDiffWithPartner[1][1]*10+csDiffAt10WithPartner
        csAt10WithPartner = csAverageWithPartner[0][1]*10
        csAt20WithPartner = csAverageWithPartner[1][1]*10 + csAt10WithPartner
    global winrateWithoutPartner
    global csDiffWithoutPartner
    global csAverageWithoutPartner
    global csDiffAt10WithoutPartneri
    global csDiffAt20WithoutPartner
    global csAt10WithoutPartner
    global csAt20WithoutPartner
    global gamesWithoutPartner
    if len(sortedMatches[1])==0:
        gamesWithoutPartner=0
    else:
        gamesWithoutPartner = len(sortedMatches[1])
        winrateWithoutPartner = rr.calculateWinrate(sortedMatches[1], summonerName)
        csDiffWithoutPartner = rr.calculateCSDiffAverage(sortedMatches[1], summonerName)
        csAverageWithoutPartner = rr.calculateCSAverage(sortedMatches[1], summonerName)
        print(csAverageWithoutPartner)
        csDiffAt10WithoutPartner = csDiffWithoutPartner[0][1]*10
        csDiffAt20WithoutPartner = csDiffWithoutPartner[1][1]*10+csDiffAt10WithoutPartner
        csAt10WithoutPartner = csAverageWithoutPartner[0][1]*10
        csAt20WithoutPartner = csAverageWithoutPartner[1][1]*10 + csAt10WithoutPartner
    
    
    
    
winrate = 0
csDiff = 0
csAverage = 0
csAt10 = 0
csAt20 = 0
csDiffAt10 = 0
csDiffAt20 = 0

partner = 'error'
winrateWithPartner = 0 
winrateWithoutPartner = 0
csDiffwithPartner = 0
csDiffWithoutPartner = 0
csAverageWithPartner = 0
csAverageWithoutPartner = 0
csAt10WithPartner = 0
csAt10WithoutPartner = 0
csAt20WithPartner = 0
csAt20WithoutPartner = 0
csDiffAt10WithPartner = 0
csDiffAt10WithoutPartner = 0
csDiffAt20WithPartner = 0
csDiffAt20WithoutPartner = 0
gamesWithPartner = 0
gamesWithoutPartner = 0    
summonerName = 'errorSummonerName'
api = 'errorAPI'
lane = 'errorLane'
mode = 'errorMode'
season='errorSeason'
Games =[]
        
app = App()

app.mainloop()  

#dataApp = DataApp()
#
#dataApp.mainloop()
#
#dataApp2 = DataApp2()
#
#dataApp2.mainloop()