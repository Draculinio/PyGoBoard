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

#---------------------------------------------------
#------PARSER---------------------------------------
#---------------------------------------------------
from goban import *

class Parser():
    def __init__(self):
        self.path=""
        self.game=[] #this will have the game itself
        self.goban=Goban()
        self.jugadas={"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19}
        self.coordenadax={"a":"a","b":"b","c":"c","d":"d","e":"e","f":"f","g":"g","h":"h","i":"j","j":"k","k":"l","l":"m","m":"n","n":"o","o":"p","p":"q","q":"r","r":"s","s":"t"}
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
