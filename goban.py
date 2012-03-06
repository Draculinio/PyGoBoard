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

#----------------------------------------------
#--GOBAN
#-Class with the board
#----------------------------------------------

class Goban():
    def __init__(self):
        self.asociativa=["x","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","x"]
        self.coordx=["a","b","c","d","e","f","g","h","j","k","l","m","n","o","p","q","r","s","t"]
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

    #def coordinate(self,jugada): #Retorna una posicion coordenada dada una jugada