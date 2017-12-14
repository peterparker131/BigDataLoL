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

import numpy as np

import Zeug as zg

import matplotlib as mp

mp.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg



largeFont = ('Verdana', 14)

class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)   #open a tkinter window
        self.geometry('1066x600')
        
        #general variables
        self.summonerName = 'errorSummonerName'
        self.api = 'errorAPI'
        self.lane = 'errorLane'
        self.mode = 'errorMode'
        self.season='errorSeason'
        self.Games =[]
        
        #Variables for Solo Analysis
        self.winrate = 0
        self.csDiff = 0
        self.csAverage = 0
        self.csAt10Min  = 0
        self.csAt20Min  = 0
        self.csDiffAt10Min  = 0 
        self.csDiffAt20Min  = 0
        self.Games = []
        
        #Variables for partner analysis
        self.partner = 'error'
        self.winrateWithPartner = 0 
        self.winrateWithoutPartner = 0
        self.csDiffwithPartner = 0
        self.csDiffWithoutPartner = 0
        self.csAverageWithPartner = 0
        self.csAverageWithoutPartner = 0
        self.csAt10MinWithPartner = 0
        self.csAt10MinWithoutPartner = 0
        self.csAt20MinWithPartner = 0
        self.csAt20MinWithoutPartner = 0
        self.csDiffAt10MinWithPartner = 0
        self.csDiffAt10MinWithoutPartner = 0
        self.csDiffAt20MinWithPartner = 0
        self.csDiffAt20MinWithoutPartner = 0
        self.gamesWithPartner = []
        self.gamesWithoutPartner = []
        
        #variables for improvement analysis
        self.winratePackages = []
        self.csAt10Packages = []
        self.csAt20Packages = []
        self.csDiffAt10Packages = []
        self.csDiffAt20Packages = []
        self.csDiffPackages = []
        self.csAveragePackages = []
        
        #ContainerForTKinterObjects
        self.conclusionLabel = {}
        self.conclusionPartnerLabel = {}
        self.buttons = {}
        self.packageLabel = {}
        
        #Sets properties of all frames
        container = tk.Frame(self)              
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        #dictionary with all frames inside
        self.frames = {}
        
        #creates all frames using the properties of container
        for F in (startPage, findGames, apiQuestion, findLane, calculate, conclusion, addPartner, conclusionWithPartner, winrateImprovement, csImprovement):
            frame = F(container, self)        
            self.frames[F] = frame       
            frame.grid(row=0, column=0, sticky='nsew')
        
        #Sets starting Frame
        self.showFrame(startPage)
        
    #Placed Label. Does this when called. Allowes to use changed variables from above
    def placeLabel(self, label, textStuff, var):
        label.config(text = textStuff + str(var))
        label.pack()
        
    #Place Button. Allowes to create button at call and not on initialization of App
    def placeButton(self, button, Text, var):
        button.config(text = Text, command=var)
        button.pack()
        
    #Bings a frame to the front
    def showFrame(self, cont):
         frame = self.frames[cont]
         frame.tkraise()
         
    #Closes the App
    def close(self):
        self.root.destroy()
        
    #Does some weird shit. Basically creates a frame and puts it into the old one
    def addFrame(self, name):
        container = tk.Frame(self)              #pick a frame containing all windows 
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        frame = name(container, self)
        self.frames[name] = frame
        frame.grid(row=0, column=0, sticky='nsew')
        
    #saveData for offline working
    def saveData(data):
        np.savetxt('matchInfos', data)
         
        
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
        self.gameModeLocal = tk.StringVar()
        self.summonerNameLocal = tk.StringVar()
        self.seasonLocal = tk.StringVar()
        
        labelSummonerName = tk.Label(self, text="Please enter your summoner name:")
        labelSummonerName.pack()
        entrySummonerName = tk.Entry(self, textvariable=self.summonerNameLocal, width=30)
        entrySummonerName.pack()
        
        labelGameMode = tk.Label(self, text="Please enter a game Mode from the following List:")
        labelGameMode.pack()
        
        radioGameMode1 = tk.Radiobutton(self, text="Ranked Solo/Duo Queue", variable=self.gameModeLocal, value="Ranked Solo/Duo Queue").pack()
        radioGameMode1 = tk.Radiobutton(self, text="Ranked Flex Queue", variable=self.gameModeLocal, value= "Ranked Flex Queue").pack()
        radioGameMode1 = tk.Radiobutton(self, text="Normal Blind Pick", variable=self.gameModeLocal, value="Normal Blind Pick").pack()
        radioGameMode1 = tk.Radiobutton(self, text="Normal Draft Pick", variable=self.gameModeLocal, value="Normal Draft Pick").pack()
        
        labelSeason = tk.Label(self, text="Please enter a season. The following Seasons are available:")
        labelSeason.pack()
        
        radioSeason1 = tk.Radiobutton(self, text="2014/2015", variable=self.seasonLocal, value="2014/2015").pack()
        radioSeason1 = tk.Radiobutton(self, text="2015/2016", variable=self.seasonLocal, value= "2015/2016").pack()
        radioSeason1 = tk.Radiobutton(self, text="2016/2017", variable=self.seasonLocal, value="2016/2017").pack()
        radioSeason1 = tk.Radiobutton(self, text="2017/2018", variable=self.seasonLocal, value="2017/2018").pack()

        button1 = tk.Button(self, text="Back to Start",
                            command=lambda: controller.showFrame(startPage))
        button1.pack()
               
        button2 = tk.Button(self, text="Continue",
                            command=lambda: merge3Functions(getMode, getSummonerName, getSeason, findLane, self.controller, self.gameModeLocal, self.summonerNameLocal, self.seasonLocal))
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
                            command=lambda: mergeFunctionWithInit(getLane, calculate, self.controller, self.Lane))
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

        button1 = tk.Button(self, text="Back to Start",
                            command=lambda: controller.showFrame(startPage))
        button1.pack()
               
        button2 = tk.Button(self)
        controller.buttons['calculateButton'] = button2
        
        button3 = tk.Button(self, text="Back",
                            command=lambda: controller.showFrame(findLane))
        button3.pack()
        
        button3 = tk.Button(self)
        controller.buttons['loadButton'] = button3

        
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
        
        labelDescription = tk.Label(self)
        controller.conclusionLabel['Description'] = labelDescription
        
        labelMain = tk.Label(self)
        controller.conclusionLabel['gameNumber'] = labelMain
        labelWinrate = tk.Label(self)
        controller.conclusionLabel['winrate'] = labelWinrate
        labelcsDiffAt10Min = tk.Label(self)
        controller.conclusionLabel['csDiffAt10Min'] = labelcsDiffAt10Min
        labelcsDiffAt20Min = tk.Label(self)
        controller.conclusionLabel['csDiffAt20Min'] =  labelcsDiffAt20Min
        labelcsAt10Min = tk.Label(self)
        controller.conclusionLabel['csAt10Min'] = labelcsAt10Min
        labelcsAt20Min = tk.Label(self)
        controller.conclusionLabel['csAt20Min'] = labelcsAt20Min
        
        
        button1 = tk.Button(self, text="Analyze these Matches by Partner",
                            command=lambda: controller.showFrame(addPartner))
        button1.pack()
        
        buttonImprovements = tk.Button(self, text='Analyze your latest improvements',
                                       command=lambda: mergePackageAnalysis(analyzePackages, winrateImprovement, self.controller, controller.Games))
        buttonImprovements.pack()
        
        buttonQuit = tk.Button(self, text="Quit",
                            command=lambda: controller.destroy())
        buttonQuit.pack()
        
class winrateImprovement(tk.Frame):
    
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
        
        labelExplanation = tk.Label(self, text=' For the following analysis we split your most recent games into packages of 20 games per package. We analyze now each package to give you an overview over your latest improvements')
        labelExplanation.pack()
        
        labelWinratePackage = tk.Label(self)
        controller.packageLabel['winrate'] = labelWinratePackage
        
        #inverts list
        reshuffleWinrate = []
        i = 1
        while i <= len(controller.winratePackages):
            reshuffleWinrate = reshuffleWinrate + [controller.winratePackages[-i]]
        
        #Hier kommt ein MatplotLib Graph rein
        
        winrateFigure = mp.figure.Figure(figsize=(1,1), dpi=100)
        fig = winrateFigure.add_subplot(111)
        fig.plot(reshuffleWinrate, 'bo')
        
        winrateCanvas = FigureCanvasTkAgg(winrateFigure, self)
        winrateCanvas.show()
        winrateCanvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        winrateCanvas._tkcanvas.pack()
        
        
        buttonCSAnalysis = tk.Button(self)
        controller.buttons['csAnalysis'] = buttonCSAnalysis
        
        
class csImprovement(tk.Frame):
    
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
        
        labelExplanation = tk.Label(self, text='Now we will analyse your overall cs development aswell as your cs development compared to your lane opponent.')
        labelExplanation.pack()
        
        labelcsAt10Package = tk.Label(self)
        controller.packageLabel['csAt10'] = labelcsAt10Package
        
        labelcsAt20Package = tk.Label(self)
        controller.packageLabel['csAt20'] = labelcsAt20Package
        
        labelcsDiffAt10Package = tk.Label(self)
        controller.packageLabel['csDiffAt10'] = labelcsDiffAt10Package
        
        labelcsDiffAt20Package = tk.Label(self)
        controller.packageLabel['csDiffAt20'] = labelcsDiffAt20Package
        
        buttonBackToConclusion = tk.Button(self)
        controller.buttons['backToConclusionFromAnalysis'] = buttonBackToConclusion
        
        buttonQuit = tk.Button(self)
        controller.buttons['quitFromAnalysis'] = buttonQuit
        
        #Hier kommen noch kleine Matplotlib Graphen hin zu jedem csWert hin. 
        
        
        
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
                            command=lambda: mergeGameListWithPartner(findGameListWithPartner, conclusionWithPartner, self.controller, self.partner.get(), controller.summonerName))
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
        
        labelDescription = tk.Label(self)
        controller.conclusionPartnerLabel['Description'] = labelDescription
        
        labelgameNumberWithPartner = tk.Label(self)
        controller.conclusionPartnerLabel['gameNumberWithPartner'] = labelgameNumberWithPartner
        labelWinrateWithPartner = tk.Label(self)
        controller.conclusionPartnerLabel['winrateWithPartner'] = labelWinrateWithPartner
        labelcsDiffAt10MinWithPartner = tk.Label(self)
        controller.conclusionPartnerLabel['csDiffAt10MinWithPartner'] = labelcsDiffAt10MinWithPartner
        labelcsDiffAt20MinWithPartner = tk.Label(self)
        controller.conclusionPartnerLabel['csDiffAt20MinWithPartner'] = labelcsDiffAt20MinWithPartner
        
        labelBlankSpace =tk.Label(self,)
        controller.conclusionPartnerLabel['blankSpace'] = labelBlankSpace
        
        labelgameNumberWithoutPartner = tk.Label(self)
        controller.conclusionPartnerLabel['gameNumberWithoutPartner'] = labelgameNumberWithoutPartner
        labelWinrateWithoutPartner = tk.Label(self)
        controller.conclusionPartnerLabel['winrateWithoutPartner'] = labelWinrateWithoutPartner
        labelcsDiffAt10MinWithoutPartner = tk.Label(self)
        controller.conclusionPartnerLabel['csDiffAt10MinWithoutPartner'] = labelcsDiffAt10MinWithoutPartner
        labelcsDiffAt20MinWithoutPartner = tk.Label(self)
        controller.conclusionPartnerLabel['csDiffAt20MinWithoutPartner'] = labelcsDiffAt20MinWithoutPartner
        
        button1 = tk.Button(self, text="Quit",
                            command=lambda: controller.destroy())
        button1.pack()
        
        button2 = tk.Button(self, text="Back",
                            command=lambda: controller.showFrame(addPartner))
        button2.pack()
    
    
def getApi(name, controller):
    var=name.get()
    controller.api = var   
    
def getMode(name, controller):
    var=name.get()
    controller.mode = var  
    
def getLane(name, controller):
    var=name.get()
    controller.lane = var  
    
def getSummonerName(name, controller):
    var=name.get()
    controller.summonerName = var 
    
def getSeason(name, controller):
    var=name.get()
    controller.season = var 
    
def mergeFunction(f, window, controller, argument1):
    f(argument1, controller)
    controller.showFrame(window)
    
def mergeFunctionWithInit(f, window, controller, argument1):
    f(argument1, controller)
    controller.placeButton(controller.buttons['calculateButton'], "Calculate Stats",
                            lambda: mergeGameList(findGameList, conclusion, controller, controller.summonerName, controller.api, controller.lane, controller.mode, controller.season))
    controller.placeButton(controller.buttons['loadButton'], "load Infos",
                            lambda: mergeDataAndAnalyze(conclusion, controller, 'Stringtheorie'))
    controller.showFrame(window)
    
def merge2Functions(f, g, window, controller, argument1, argument2):
    f(argument1, controller)
    g(argument2, controller)
    controller.variable2 = argument2.get()
    controller.showFrame(window)
    
def merge3Functions(f, g, h, window, controller, argument1, argument2, argument3):
    f(argument1, controller)
    g(argument2, controller)
    h(argument3, controller)
    controller.showFrame(window)
    
def mergePackageAnalysis(f, window, controller, argument1):
    f(argument1, controller)
    controller.placeLabel(controller.packageLabel['winrate'], 'Your winrates starting with your latest games are: ', str(controller.winratePackages,2))
    controller.placeButton(controller.buttons['csAnalysis'], 'Proceed to cs Analysis',
                           lambda: controller.showFrame(csImprovement))
    controller.placeLabel(controller.packageLabel['csDiffAt10'], 'Your cs difference after 10 min starting with your latest games are: ', str(controller.csAt10Packages,2))
    controller.placeLabel(controller.packageLabel['csDiffAt20'], 'Your cs difference after 20 min starting with your latest games are: ', str(controller.csAt20Packages,2))
    controller.placeLabel(controller.packageLabel['csAt10'], 'Your overall cs after 10 min starting with your latest games are: ', str(controller.csAt10Packages,2))
    controller.placeLabel(controller.packageLabel['csAt20'], 'Your overall cs after 20 min starting with your latest games are: ', str(controller.csAt20Packages,2))
    controller.placeButton(controller.buttons['backToConclusionFromAnalysis'], 'Back to overall conclusion',
                           lambda: controller.showFrame(conclusion))
    controller.placeButton(controller.buttons['quitFromAnalysis'], 'Quit',
                           lambda: controller.close())
    controller.showFrame(window)
    
def mergeGameList(f, window, controller, argument1, argument2, argument3, argument4, argument5):
    f(argument1, argument2, argument3, argument4, argument5, controller)
    controller.placeLabel(controller.conclusionLabel['Description'], "The following Data could be analyzed:", '')
    controller.placeLabel(controller.conclusionLabel['gameNumber'], 'We analyzed the following number of games:   ', len(controller.Games))
    controller.placeLabel(controller.conclusionLabel['winrate'], 'Your winrate is:   ', str(round(controller.winrate,2) ) )
    controller.placeLabel(controller.conclusionLabel['csDiffAt10Min'], 'Your CS difference at 10 min is   :   ', str(round(controller.csDiffAt10Min,2)) )
    controller.placeLabel(controller.conclusionLabel['csDiffAt20Min'], 'Your CS difference at 20 min is   :   ', str(round(controller.csDiffAt20Min,2)) )
    controller.placeLabel(controller.conclusionLabel['csAt10Min'], 'This leads to an absolute value of ', str(round(controller.csAt10Min,2)) + ' at 10 min.')
    controller.placeLabel(controller.conclusionLabel['csAt20Min'], ' and ', str(round(controller.csAt20Min,2)) + ' at 20 min.')
    controller.showFrame(window)
#    controller.destroy()
    
def mergeGameListWithPartner(f, window, controller, argument1, argument2):
    f(argument1,  argument2, controller)
    controller.placeLabel(controller.conclusionPartnerLabel['Description'], "The following Data could be analyzed:", '')
    controller.placeLabel(controller.conclusionPartnerLabel['gameNumberWithPartner'], 'We analyzed the following number of games with ' +  controller.partner +':   ', len(controller.gamesWithPartner))
    controller.placeLabel(controller.conclusionPartnerLabel['winrateWithPartner'], 'Your winrate is:   ', str(round(controller.winrateWithPartner,2)) )
    controller.placeLabel(controller.conclusionPartnerLabel['csDiffAt10MinWithPartner'], 'Your CS difference at 10 min is   :   ', str(round(controller.csDiffAt10MinWithPartner,2)) )
    controller.placeLabel(controller.conclusionPartnerLabel['csDiffAt20MinWithPartner'], 'Your CS difference at 20 min is   :   ', str(round(controller.csDiffAt20MinWithPartner,2)) )
    controller.placeLabel(controller.conclusionPartnerLabel['blankSpace'], '', '')
    controller.placeLabel(controller.conclusionPartnerLabel['gameNumberWithoutPartner'], 'We analyzed the following number of games without ' +  controller.partner +':   ', len(controller.gamesWithoutPartner))
    controller.placeLabel(controller.conclusionPartnerLabel['winrateWithoutPartner'], 'Your winrate is:   ', str(round(controller.winrateWithoutPartner,2)) )
    controller.placeLabel(controller.conclusionPartnerLabel['csDiffAt10MinWithoutPartner'], 'Your CS difference at 10 min is   :   ', str(round(controller.csDiffAt10MinWithoutPartner,2)) )
    controller.placeLabel(controller.conclusionPartnerLabel['csDiffAt20MinWithoutPartner'], 'Your CS difference at 20 min is   :   ', str(round(controller.csDiffAt20MinWithoutPartner,2)) )
    controller.showFrame(window)

      
def findGameList(summonerName, key, lane, queue, season, controller):
    print(summonerName, key, lane, queue, season)
    seasonNumber = rr.seasonList[season]
    personalData = rr.getSummonerAccountID(summonerName, key)
    print(personalData)
    summonerID = personalData['accountId']
    matchList = rr.getSpecificMatchlist(summonerID, key, rr.listOfQKeys[queue] , seasonNumber)
    matchesByLane = rr.sortMatchesToLane(matchList, 'lane')
    gameInfo = rr.getGameInfos(matchesByLane[0], key)
    controller.Games = gameInfo
    number = rr.calculateWinrate(gameInfo, summonerName)
    controller.winrate = number
    controller.csDiff = rr.calculateCSDiffAverage(gameInfo, summonerName)
    controller.csAverage = rr.calculateCSAverage(gameInfo, summonerName)
    controller.csDiffAt10Min = controller.csDiff[0][1]*10
    controller.csDiffAt20Min = controller.csDiff[1][1]*10 + controller.csDiffAt10Min
    controller.csAt10Min = controller.csAverage[0][1]*10
    controller.csAt20Min = controller.csAverage[1][1]*10 + controller.csAt10Min 
    print(gameInfo)
    
def findGameListWithPartner(Partner, summonerName, controller):
    controller.partner = Partner
    sortedMatches = rr.extractMatchesWithAnotherPartner(controller.Games, Partner)
    if len(sortedMatches[0])==0:
        controller.gamesWithPartner=[]
    else:
        controller.gamesWithPartner = sortedMatches[0]
        controller.winrateWithPartner = rr.calculateWinrate(sortedMatches[0], summonerName)
        controller.csDiffWithPartner = rr.calculateCSDiffAverage(sortedMatches[0], summonerName)
        controller.csAverageWithPartner = rr.calculateCSAverage(sortedMatches[0], summonerName)
        controller.csDiffAt10MinWithPartner = controller.csDiffWithPartner[0][1]*10
        controller.csDiffAt20MinWithPartner = controller.csDiffWithPartner[1][1]*10+ controller.csDiffAt10MinWithPartner
        controller.csAt10MinWithPartner = controller.csAverageWithPartner[0][1]*10
        controller.csAt20MinWithPartner = controller.csAverageWithPartner[1][1]*10 + controller.csAt10MinWithPartner
    if len(sortedMatches[1])==0:
        controller.gamesWithoutPartner=[]
    else:
        controller.gamesWithoutPartner = sortedMatches[1]
        controller.winrateWithoutPartner = rr.calculateWinrate(sortedMatches[1], summonerName)
        controller.csDiffWithoutPartner = rr.calculateCSDiffAverage(sortedMatches[1], summonerName)
        controller.csAverageWithoutPartner = rr.calculateCSAverage(sortedMatches[1], summonerName)
        controller.csDiffAt10MinWithoutPartner = controller.csDiffWithoutPartner[0][1]*10
        controller.csDiffAt20MinWithoutPartner = controller.csDiffWithoutPartner[1][1]*10+ controller.csDiffAt10MinWithoutPartner
        controller.csAt10MinWithoutPartner = controller.csAverageWithoutPartner[0][1]*10
        controller.csAt20MinWithoutPartner = controller.csAverageWithoutPartner[1][1]*10 + controller.csAt10MinWithoutPartner
   
def mergeDataAndAnalyze(window, controller, summName='Stringtheorie'):
    loadDataAndAnalyze(controller, summName) 
    controller.placeLabel(controller.conclusionLabel['Description'], "The following Data could be analyzed:", '')
    controller.placeLabel(controller.conclusionLabel['gameNumber'], 'We analyzed the following number of games:   ', len(controller.Games))
    controller.placeLabel(controller.conclusionLabel['winrate'], 'Your winrate is:   ', str(round(controller.winrate,2) ) )
    controller.placeLabel(controller.conclusionLabel['csDiffAt10Min'], 'Your CS difference at 10 min is   :   ', str(round(controller.csDiffAt10Min,2)) )
    controller.placeLabel(controller.conclusionLabel['csDiffAt20Min'], 'Your CS difference at 20 min is   :   ', str(round(controller.csDiffAt20Min,2)) )
    controller.placeLabel(controller.conclusionLabel['csAt10Min'], 'This leads to an absolute value of ', str(round(controller.csAt10Min,2)) + ' at 10 min.')
    controller.placeLabel(controller.conclusionLabel['csAt20Min'], ' and ', str(round(controller.csAt20Min,2)) + ' at 20 min.')
    controller.showFrame(window)

def loadDataAndAnalyze(controller, summName):
    gameInfo = zg.gameInfoLoad
    controller.Games = gameInfo
    number = rr.calculateWinrate(gameInfo, summName)
    controller.winrate = number
    controller.csDiff = rr.calculateCSDiffAverage(gameInfo, summName)
    controller.csAverage = rr.calculateCSAverage(gameInfo, summName)
    controller.csDiffAt10Min = controller.csDiff[0][1]*10
    controller.csDiffAt20Min = controller.csDiff[1][1]*10 + controller.csDiffAt10Min
    controller.csAt10Min = controller.csAverage[0][1]*10
    controller.csAt20Min = controller.csAverage[1][1]*10 + controller.csAt10Min
    
def divideMatchList(matchList, packageSize=10): #to split list into packages of packageSize of latest games
    listOfPackages = rr.divideMatchlistIntoPackages(matchList, packageSize)
    return listOfPackages

def analyzePackages(matchList, controller):
    summName = controller.summonerName
    listOfPackages = divideMatchList(matchList)
    controller.winratePackages = []
    controller.csDiffPackages = []
    controller.csAveragePackages = []
    controller.csDiffAt10Packages = []
    controller.csDiffAt20Packages = []
    controller.csAt10Packages = []
    controller.csAt20Packages = []
    counter = 0
    for package in listOfPackages:
        controller.winratePackages = controller.winratePackages + [rr.calculateWinrate(package, summName)]
        controller.csDiffPackages = controller.csDiffPackages + [rr.calculateCSDiffAverage(package, summName)]
        controller.csAveragePackages = controller.csAveragePackages + [rr.calculateCSAverage(package, summName)]
        controller.csDiffAt10Packages = controller.csDiffAt10Packages + [controller.csDiffPackages[counter][0][1]*10]
        controller.csDiffAt20Packages = controller.csDiffAt20Packages + [controller.csDiffPackages[counter][1][1]*10 + controller.csDiffAt10Packages[counter]]
        controller.csAt10Packages = controller.csAt10Packages + [controller.csAveragePackages[counter][0][1]*10]
        controller.csAt20Packages = controller.csAt20Packages + [controller.csAveragePackages[counter][1][1]*10 + controller.csAt10Packages[counter]]
        counter = counter + 1
    
        
        
        
    
    
        
app = App()

app.mainloop()  
