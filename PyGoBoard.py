#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
---------------------------------
-----------PyGoBoard-------------
---------------------------------

By Pablo Soifer -Draculinio-
stackpointerex@gmail.com

"""

import wx
import os
#import re

class Principal(wx.Frame):
    def __init__(self, parent, title):
        super(Principal, self).__init__(parent, title=title,
            size=(250, 150))

        self.SetSize((800,600))
        self.SetTitle="PyGoBoard"

        #Variables varias
        self.juego=[]
        self.puntero_jugada=0
        self.jugadas={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19}
        self.tablero= Goban()
        self.temporal=0
        self.lastmove="" #the array of the last move.

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


    def onQuit(self,event):
        self.Close()

    def onOpen(self,event):
        dlg = wx.FileDialog(self, "Choose a file", os.getcwd(), "", "*.sgf", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            mypath = os.path.basename(path)
            finalpath=path+mypath
            finalpath=finalpath[1:len(finalpath)]
            file=open(path,"r")
            SuccessFile=file.read(2)
            if(SuccessFile!='(;'):
                wx.MessageBox("Invalid File",SuccessFile,wx.OK)
            #Ahora salgo a leer los datos del partido
            else:
                alcanzado=0
                while alcanzado!=2:
                    linea=file.readline()
                    if("PB[" in linea):
                        cantidad=len(linea)
                        wx.StaticText(self,-1,linea[3:cantidad-2],(600,70))
                        alcanzado=alcanzado+1
                    if("PW[" in linea):
                        cantidad=len(linea)
                        wx.StaticText(self,-1,linea[3:cantidad-2],(700,70))
                    if (linea==""):
                        alcanzado=2
                file.close()
                file=open(path,"r")
                #Armo un array con todo el partido
                alcanzado=0
                fin_de_archivo=0
                flag_cantidad=0
                while fin_de_archivo==0:
                    caracter=file.read(1)
                    self.juego.append(caracter)
                    if(caracter==""):
                        fin_de_archivo=1
                #Quito lo que no me interesa
                cant=0
                temp=[]
                for i in range(0,len(self.juego)-1):
                    if(self.juego[i]==';'):
                        cant=cant+1
                    if(cant>=2):
                        temp.append(self.juego[i])
                self.juego=temp
            file.close()
            self.forward.Enable()
        dlg.Destroy()

    def Posterior(self,event):
        activar=""
        self.puntero_jugada=self.puntero_jugada+1
        flag_encontrado=0 #Encontró la jugada
        puntero_busqueda=0 #Busqueda dentro del vector
        puntero_cantidad=0 #cuantos ; encontro, al ser igual que la cantidad de jugadas es esa.
        while flag_encontrado==0:
            if (self.juego[puntero_busqueda]==';'):
                puntero_cantidad=puntero_cantidad+1
                if(puntero_cantidad==self.puntero_jugada): #Encontro la jugada
                    flag_encontrado=1
                    for i in range(1,6):
                        activar=activar+self.juego[puntero_busqueda+i]
            puntero_busqueda=puntero_busqueda+1
            #wx.StaticText(self,-1,activar,(500,500))
            self.lastmove=activar
        wx.StaticText(self,-1,activar,(500,500))
        self.mapear(activar)
        if(self.back.Enable()=='False'):
            self.back.Enable()

    def Previous(self,event):
        activar=""
        flag_encontrado=0
        puntero_busqueda=0
        puntero_cantidad=0
        #First, remove last move.
        self.desmapear(self.lastmove)
        #go back one move
        self.puntero_jugada=self.puntero_jugada-1
        #and put in last move the actual last move
        if(self.puntero_jugada!=0): #Si no es la primer jugada
            while flag_encontrado==0:
                if (self.juego[puntero_busqueda]==';'):
                    puntero_cantidad=puntero_cantidad+1
                    if(puntero_cantidad==self.puntero_jugada): #Encontro la jugada
                        flag_encontrado=1
                        for i in range(1,6):
                            activar=activar+self.juego[puntero_busqueda+i]
                puntero_busqueda=puntero_busqueda+1
        else: #First move, so I disable back button
            self.back.Disable()
        wx.StaticText(self,-1,activar,(500,500))
        self.lastmove=activar

    def mapear(self,jugada): #cambia valores en el tablero.
        #0=Nada, 1=Blanco 2=Negro 3=Borde
        jx=self.jugadas[jugada[2]]
        jy=self.jugadas[jugada[3]]
        if(jugada[0]=="B"): #negro
            self.tablero.set_valor(jx,jy,2)
            opuesto=1
        else: #blanco
            self.tablero.set_valor(jx,jy,1)
            opuesto=2
        print opuesto
        #Busco que a los costados haya algo color opuesto como para ver si lo mato
        if(self.tablero.get_valor(jx-1,jy)==opuesto):
            grupo=self.tablero.buscar_grupos(jx-1,jy)
            cant_lib=self.tablero.contar_libertades(grupo)
            print "Izquierda"+str(cant_lib)
            if(cant_lib==0):
                for i in range(0,len(grupo)):
                    self.tablero.set_valor(self.tablero.posiciones(grupo[i][0]),self.tablero.posiciones(grupo[i][1]),0)

        if(self.tablero.get_valor(jx+1,jy)==opuesto):
            grupo=self.tablero.buscar_grupos(jx+1,jy)
            cant_lib=self.tablero.contar_libertades(grupo)
            print "Derecha"+str(cant_lib)
            if(cant_lib==0):
                for i in range(0,len(grupo)):
                    self.tablero.set_valor(self.tablero.posiciones(grupo[i][0]),self.tablero.posiciones(grupo[i][1]),0)

        if(self.tablero.get_valor(jx,jy-1)==opuesto):
            grupo=self.tablero.buscar_grupos(jx,jy-1)
            cant_lib=self.tablero.contar_libertades(grupo)
            print "Arriba"+str(cant_lib)
            if(cant_lib==0):
                for i in range(0,len(grupo)):
                    self.tablero.set_valor(self.tablero.posiciones(grupo[i][0]),self.tablero.posiciones(grupo[i][1]),0)

        if(self.tablero.get_valor(jx,jy+1)==opuesto):
            grupo=self.tablero.buscar_grupos(jx,jy+1)
            cant_lib=self.tablero.contar_libertades(grupo)
            print "Abajo"+str(cant_lib)
            if(cant_lib==0):
                for i in range(0,len(grupo)):
                    self.tablero.set_valor(self.tablero.posiciones(grupo[i][0]),self.tablero.posiciones(grupo[i][1]),0)
        self.Refresh()

    def desmapear(self,jugada): #desmapea una jugada
        jx=self.jugadas[jugada[2]]
        jy=self.jugadas[jugada[3]]
        self.tablero.set_valor(jx,jy,0)
        self.Refresh()


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


if __name__ == '__main__':
    app = wx.App()
    Principal(None, 'PyGoBoard')
    app.MainLoop()