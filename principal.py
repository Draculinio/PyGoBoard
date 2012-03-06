#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      psoifer
#
# Created:     06/03/2012
# Copyright:   (c) psoifer 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import wx
import os

import parserD
from goban import *
#from goban import *

class Principal(wx.Frame):
    def __init__(self, parent, title):
        super(Principal, self).__init__(parent, title=title,
            size=(250, 150))

        self.SetSize((800,600))
        self.SetTitle="PyGoBoard"
        self.parse=parserD.Parser()
        #self.parse=parser.Parser()
        #Variables varias
        self.juego=[]
        self.puntero_jugada=0
        self.jugadas={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19}
        self.tablero=Goban()
        self.temporal=0
        self.lastmove="" #the array of the last move.
        #self.path="" #For the path that all command functions will take
        #Menu
        menubar=wx.MenuBar()
        file=wx.Menu()
        help=wx.Menu()
        file.Append(wx.ID_OPEN,'&Open','Opens a game')
        file.Append(wx.ID_EXIT,'&Exit','Exits the application')
        help.Append(wx.ID_HELP,'&Help','Help')
        help.Append(wx.ID_ABOUT,'&About','About')
        self.Bind(wx.EVT_MENU,self.onQuit,id=wx.ID_EXIT)
        self.Bind(wx.EVT_MENU,self.onOpen,id=wx.ID_OPEN)
        self.Bind(wx.EVT_MENU,self.onAbout,id=wx.ID_ABOUT)
        menubar.Append(file,'&File')
        menubar.Append(help,'&Help')
        self.SetMenuBar(menubar)

        #Botones
        self.back=wx.Button(self,100,"<<",(50,500))
        self.forward=wx.Button(self,101,">>",(350,500))
        self.back.Bind(wx.EVT_BUTTON, self.Previous, id=100)
        self.forward.Bind(wx.EVT_BUTTON, self.Posterior, id=101)
        self.forward.Disable()
        self.back.Disable()
        #Dibujar pantalla
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        #Textos
        wx.StaticText(self,-1,'File: ',(600,20))
        TextBlack=wx.StaticText(self,-1,'BLACK',(600,50))
        TextBlack.SetBackgroundColour('#000000')
        TextBlack.SetForegroundColour('#FFFFFF')
        TextWhite=wx.StaticText(self,-1,'WHITE',(700,50))
        TextWhite.SetBackgroundColour('#FFFFFF')
        TextWhite.SetForegroundColour('#000000')
        wx.StaticText(self,-1,'Captures',(600,100))
        wx.StaticText(self,-1,'Captures',(700,100))
        self.escribir_coordenadas()
        titlefont = wx.Font(16, wx.NORMAL, wx.NORMAL, wx.NORMAL)
        subtitlefont=wx.Font(8, wx.NORMAL, wx.NORMAL, wx.BOLD)
        titulo=wx.StaticText(self,-1,'GAME DATA',(620,160))
        titulo.SetFont(titlefont)
        sub=wx.StaticText(self,-1,'Rules:',(575,230))
        sub.SetFont(subtitlefont)
        sub=wx.StaticText(self,-1,'Size:',(575,250))
        sub.SetFont(subtitlefont)
        sub=wx.StaticText(self,-1,'Time:',(575,270))
        sub.SetFont(subtitlefont)
        sub=wx.StaticText(self,-1,'OT:',(650,270))
        sub.SetFont(subtitlefont)
        sub=wx.StaticText(self,-1,'Komi:',(575,290))
        sub.SetFont(subtitlefont)
        sub=wx.StaticText(self,-1,'Result:',(575,310))
        sub.SetFont(subtitlefont)
        #Muestra
        self.Centre()
        self.Show()


    def OnPaint(self,e):
        dc=wx.PaintDC(self)
        DirectorioImagenes = os.getcwd()+"\images\g19x19.png"
        bitmap=wx.Bitmap(DirectorioImagenes)
        dc.DrawBitmap(bitmap,20,20)
        dc.SetBrush(wx.Brush('#A4A4A4'))
        dc.DrawRectangle(570,40,600,150)
        dc.DrawRectangle(570,150,600,300)
        dc.BeginDrawing()
        for x in range(1,19):
            for y in range(1,19):
                if(self.tablero.get_valor(x,y)!=0):
                    if(self.tablero.get_valor(x,y)==1):
                        dc.SetBrush(wx.Brush('#FFFFFF'))
                    if(self.tablero.get_valor(x,y)==2):
                        dc.SetBrush(wx.Brush('#000000'))
                    arraypos=[36,56,79,102,125,148,171,194,217,240,263,286,309,332,355,378,401,424,447]
                    dc.DrawCircle(arraypos[x-1],arraypos[y-1],8)

        dc.EndDrawing()

    def escribir_coordenadas(self):
        wx.StaticText(self,-1,"A",(32,6))
        wx.StaticText(self,-1,"B",(52,6))
        wx.StaticText(self,-1,"C",(75,6))
        wx.StaticText(self,-1,"D",(98,6))
        wx.StaticText(self,-1,"E",(121,6))
        wx.StaticText(self,-1,"F",(144,6))
        wx.StaticText(self,-1,"G",(167,6))
        wx.StaticText(self,-1,"H",(190,6))
        wx.StaticText(self,-1,"J",(213,6))
        wx.StaticText(self,-1,"K",(236,6))
        wx.StaticText(self,-1,"L",(259,6))
        wx.StaticText(self,-1,"M",(282,6))
        wx.StaticText(self,-1,"N",(305,6))
        wx.StaticText(self,-1,"O",(328,6))
        wx.StaticText(self,-1,"P",(351,6))
        wx.StaticText(self,-1,"Q",(374,6))
        wx.StaticText(self,-1,"R",(397,6))
        wx.StaticText(self,-1,"S",(420,6))
        wx.StaticText(self,-1,"T",(443,6))

        wx.StaticText(self,-1,"1",(6,32))
        wx.StaticText(self,-1,"2",(6,52))
        wx.StaticText(self,-1,"3",(6,75))
        wx.StaticText(self,-1,"4",(6,98))
        wx.StaticText(self,-1,"5",(6,121))
        wx.StaticText(self,-1,"6",(6,144))
        wx.StaticText(self,-1,"7",(6,167))
        wx.StaticText(self,-1,"8",(6,190))
        wx.StaticText(self,-1,"9",(6,213))
        wx.StaticText(self,-1,"10",(6,236))
        wx.StaticText(self,-1,"11",(6,259))
        wx.StaticText(self,-1,"12",(6,282))
        wx.StaticText(self,-1,"13",(6,305))
        wx.StaticText(self,-1,"14",(6,328))
        wx.StaticText(self,-1,"15",(6,351))
        wx.StaticText(self,-1,"16",(6,374))
        wx.StaticText(self,-1,"17",(6,397))
        wx.StaticText(self,-1,"18",(6,420))
        wx.StaticText(self,-1,"19",(6,443))

    def onQuit(self,event):
        self.Close()

    def onOpen(self,event):
        dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", "*.sgf", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.parse.set_file(path)
            if(self.parse.verify_file()==False):
                wx.MessageBox("Invalid File",SuccessFile,wx.OK)
            #Ahora salgo a leer los datos del partido
            else:
                #delete the fields so if I open a new game in the middle of one, the names are not overwrited
                wx.StaticText(self,-1,"                        ",(600,70))
                wx.StaticText(self,-1,"                        ",(700,70))
                playerw=self.parse.search_com("PW")
                wx.StaticText(self,-1,playerw,(600,70))
                playerb=self.parse.search_com("PB")
                wx.StaticText(self,-1,playerb,(700,70))
                rules=self.parse.search_com("RU")
                wx.StaticText(self,-1,rules,(610,230))
                size=self.parse.search_com("SZ")
                wx.StaticText(self,-1,size,(610,250))
                time=self.parse.search_com("TM")
                wx.StaticText(self,-1,time,(610,270))
                overtime=self.parse.search_com("OT")
                wx.StaticText(self,-1,overtime,(680,270))
                overtime=self.parse.search_com("KM")
                wx.StaticText(self,-1,overtime,(610,290))
                result=self.parse.search_com("RE")
                wx.StaticText(self,-1,result,(615,310))
                self.parse.set_game() #Make the game array

                self.forward.Enable()
            dlg.Destroy()

    def Posterior(self,event):
        um=""
        self.puntero_jugada=self.puntero_jugada+1
        self.tablero=self.parse.parse_game(self.puntero_jugada)
        self.Refresh()
        if(self.back.Enable()=='False'):
            self.back.Enable()

    def Previous(self,event):
        self.puntero_jugada=self.puntero_jugada-1
        self.tablero=self.parse.parse_game(self.puntero_jugada)
        self.Refresh()
        if(self.puntero_jugada==0):
            self.back.Disable()

    def onAbout(self,event):
        wx.MessageBox('PyGoBoard 0.2A', 'Info', wx.OK | wx.ICON_INFORMATION)
