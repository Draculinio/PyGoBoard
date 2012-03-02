#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
---------------------------------
-----------PyGoBoard-------------
---------------------------------
Version 0.2
By Pablo Soifer -Draculinio-
stackpointerex@gmail.com

"""

import wx
import os

class Principal(wx.Frame):
    def __init__(self, parent, title):
        super(Principal, self).__init__(parent, title=title,
            size=(250, 150))

        self.SetSize((800,600))
        self.SetTitle="PyGoBoard"
        self.parser=Parser()
        #Variables varias
        self.juego=[]
        self.puntero_jugada=0
        self.jugadas={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19}
        self.tablero= Goban()
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
        wx.StaticText(self,-1,'Last Move',(800,600))
        wx.StaticText(self,-1,'Rules:',(550,350))
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
            self.parser.set_file(path)
            if(self.parser.verify_file()==False):
                wx.MessageBox("Invalid File",SuccessFile,wx.OK)
            #Ahora salgo a leer los datos del partido
            else:
                #delete the fields so if I open a new game in the middle of one, the names are not overwrited
                wx.StaticText(self,-1,"                        ",(600,70))
                wx.StaticText(self,-1,"                        ",(700,70))
                playerw=self.parser.search_com("PW")
                wx.StaticText(self,-1,playerw,(600,70))
                playerb=self.parser.search_com("PB")
                wx.StaticText(self,-1,playerb,(700,70))
                reglas=self.parser.search_com("RU")
                wx.StaticText(self,-1,reglas,(600,350))
                self.parser.set_game() #Make the game array
                self.forward.Enable()
            dlg.Destroy()

    def Posterior(self,event):
        self.puntero_jugada=self.puntero_jugada+1
        self.tablero=self.parser.parse_game(self.puntero_jugada)
        self.Refresh()
        if(self.back.Enable()=='False'):
            self.back.Enable()

    def Previous(self,event):
        self.puntero_jugada=self.puntero_jugada-1
        self.tablero=self.parser.parse_game(self.puntero_jugada)
        self.Refresh()
        if(self.puntero_jugada==0):
            self.back.Disable()

    def onAbout(self,event):
        wx.MessageBox('PyGoBoard 0.2', 'Info', wx.OK | wx.ICON_INFORMATION)

#----------------------------------------------
#--GOBAN
#-Class with the board
#----------------------------------------------

class Goban():
    def __init__(self):
        self.asociativa=["x","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","x"]
        self.tablero=[[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
                [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
                [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
                [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
                [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
                [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
                [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
                [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
                [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
                [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
                [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
                [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
                [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
                [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
                [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
                [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
                [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
                [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
                [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
                [3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
                [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]]

    def set_valor(self,px,py,valor):
        self.tablero[px][py]=valor

    def get_valor(self,px,py):
        return self.tablero[px][py]

    def reset_goban(self):
        for i in range (1,20):
            for j in range(1,20):
                self.tablero[i][j]=0

    def buscar_grupos(self,x,y):
        posicion=0
        color=self.get_valor(x,y)
        grupo=[]
        agregado=self.asociativa[x]+self.asociativa[y]
        grupo.append(agregado)
        largo_array=len(grupo)
        while posicion<largo_array:
            posx=self.posiciones(grupo[posicion][0])
            posy=self.posiciones(grupo[posicion][1])

            #-----BUSQUEDA PARA AGREGAR ELEMENTOS AL GRUPO-----
            #Busco izquierda
            if (self.get_valor(posx,posy-1)==color): #El que esta arriba es del color
                #Busco que no este incluido ya
                flag_estaba=0
                for b in range(0,len(grupo)):
                    if(grupo[b]==self.asociativa[posx]+self.asociativa[posy-1]): #Lo encontro y no lo meto
                        flag_estaba=1
                if(flag_estaba==0):
                    grupo.append(self.asociativa[posx]+self.asociativa[posy-1])

            #Busco derecha
            if (self.get_valor(posx,posy+1)==color): #El que esta arriba es del color
                #Busco que no este incluido ya
                flag_estaba=0
                for b in range(0,len(grupo)):
                    if(grupo[b]==self.asociativa[posx]+self.asociativa[posy+1]): #Lo encontro y no lo meto
                        flag_estaba=1
                if(flag_estaba==0):
                    grupo.append(self.asociativa[posx]+self.asociativa[posy+1])

            #Busco arriba
            if (self.get_valor(posx-1,posy)==color): #El que esta arriba es del color
                #Busco que no este incluido ya
                flag_estaba=0
                for b in range(0,len(grupo)):
                    if(grupo[b]==self.asociativa[posx-1]+self.asociativa[posy]): #Lo encontro y no lo meto
                        flag_estaba=1
                if(flag_estaba==0):
                    grupo.append(self.asociativa[posx-1]+self.asociativa[posy])

            #Busco abajo
            if (self.get_valor(posx+1,posy)==color): #El que esta arriba es del color
                #Busco que no este incluido ya
                flag_estaba=0
                for b in range(0,len(grupo)):
                    if(grupo[b]==self.asociativa[posx+1]+self.asociativa[posy]): #Lo encontro y no lo meto
                        flag_estaba=1
                if(flag_estaba==0):
                    grupo.append(self.asociativa[posx+1]+self.asociativa[posy])
            #-----FIN BUSQUEDA PARA AGREGAR ELEMENTOS AL GRUPO-----
            posicion=posicion+1
            largo_array=len(grupo)
        return grupo

    def contar_libertades(self,grupo):
        cuenta_libertades=0
        for i in range(0,len(grupo)):
            posx=self.posiciones(grupo[i][0])
            posy=self.posiciones(grupo[i][1])
            if (self.get_valor(posx,posy-1)==0): #El que esta arriba esta vacio
                cuenta_libertades=cuenta_libertades+1
            if (self.get_valor(posx,posy+1)==0): #El que esta abajo esta vacio
                cuenta_libertades=cuenta_libertades+1
            if (self.get_valor(posx-1,posy)==0): #El que esta a la derecha esta vacio
                cuenta_libertades=cuenta_libertades+1
            if (self.get_valor(posx+1,posy)==0): #El que esta arriba esta vacio
                cuenta_libertades=cuenta_libertades+1
        return cuenta_libertades

    def posiciones(self,posicion): #Retorna una posicion numerica dada una letra
        a=0
        for i in range(0,20):
            if(self.asociativa[i]==posicion):
                a=i
        return a
#---------------------------------------------------
#------PARSER---------------------------------------
#---------------------------------------------------

class Parser():
    def __init__(self):
        self.path=""
        self.game=[] #this will have the game itself
        self.goban=Goban()
        self.jugadas={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19}

    def set_file(self,archivo):
        self.path=archivo

    def set_game(self):
        file=open(self.path,"r")
        #Armo un array con todo el partido
        temp=[]
        alcanzado=0
        cant=0
        self.game=file.read()
        file.close()
        #Quito lo que no me interesa
        for i in range(0,len(self.game)):
            if(self.game[i]==';'):
                cant=cant+1
            if(cant>=2):
                temp.append(self.game[i])
        self.game=temp

    def verify_file(self): #Verifies if the file is a valid sgf file
        retorno=False
        file=open(self.path,"r")
        SuccessFile=file.read(2)
        if(SuccessFile=='(;'):
            retorno=True
        file.close()
        return retorno

    def search_com(self,comando): #Searches for a command
        retorno=""
        file=open(self.path,"r")
        encontrado=0
        while encontrado==0:
            linea=file.readline()
            if(comando+"[" in linea):
                encontrado=1
                for i in range(0,len(linea)):
                    if(linea[i]=="[" and linea[i-1]==comando[1] and linea[i-2]==comando[0]):
                        j=i+1
                        while linea[j]!="]":
                            retorno=retorno+linea[j]
                            j=j+1
            if(linea==""):
                retorno="-"
                encontrado=1
        file.close()
        return retorno

    def parse_game(self,move_number):
        self.goban.reset_goban()
        puntero_busqueda=0
        for i in range(0,move_number):
            activar=""
            flag_encontrado=False
            while flag_encontrado!=True:
                if(self.game[puntero_busqueda]==";"):
                    flag_encontrado=True
                    for j in range(1,6):
                        activar=activar+self.game[puntero_busqueda+j]
                    self.mapear(activar)
                puntero_busqueda=puntero_busqueda+1
        return self.goban

    def mapear(self,jugada): #cambia valores en el tablero.
        #0=Nada, 1=Blanco 2=Negro 3=Borde
        jx=self.jugadas[jugada[2]]
        jy=self.jugadas[jugada[3]]
        if(jugada[0]=="B"): #negro
            self.goban.set_valor(jx,jy,2)
            opuesto=1
        else: #blanco
            self.goban.set_valor(jx,jy,1)
            opuesto=2
        #Busco que a los costados haya algo color opuesto como para ver si lo mato
        if(self.goban.get_valor(jx-1,jy)==opuesto):
            grupo=self.goban.buscar_grupos(jx-1,jy)
            cant_lib=self.goban.contar_libertades(grupo)
            if(cant_lib==0):
                for i in range(0,len(grupo)):
                    self.goban.set_valor(self.goban.posiciones(grupo[i][0]),self.goban.posiciones(grupo[i][1]),0)

        if(self.goban.get_valor(jx+1,jy)==opuesto):
            grupo=self.goban.buscar_grupos(jx+1,jy)
            cant_lib=self.goban.contar_libertades(grupo)
            if(cant_lib==0):
                for i in range(0,len(grupo)):
                    self.goban.set_valor(self.goban.posiciones(grupo[i][0]),self.goban.posiciones(grupo[i][1]),0)

        if(self.goban.get_valor(jx,jy-1)==opuesto):
            grupo=self.goban.buscar_grupos(jx,jy-1)
            cant_lib=self.goban.contar_libertades(grupo)
            if(cant_lib==0):
                for i in range(0,len(grupo)):
                    self.goban.set_valor(self.goban.posiciones(grupo[i][0]),self.goban.posiciones(grupo[i][1]),0)

        if(self.goban.get_valor(jx,jy+1)==opuesto):
            grupo=self.goban.buscar_grupos(jx,jy+1)
            cant_lib=self.goban.contar_libertades(grupo)
            if(cant_lib==0):
                for i in range(0,len(grupo)):
                    self.goban.set_valor(self.goban.posiciones(grupo[i][0]),self.goban.posiciones(grupo[i][1]),0)
        #self.Refresh()

#-------------------------------------------------
#---------------------MAIN------------------------
#-------------------------------------------------

if __name__ == '__main__':
    app = wx.App()
    Principal(None, 'PyGoBoard')
    app.MainLoop()