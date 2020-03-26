#!/usr/bin/python3
# Integrantes del equipo:
#   Alcaraz Biebrich Manuel Alejandro
#   Encinas Alegre Jorge Carlos
#   Romero Andrade Paula Cristina
# Fecha: 20 de Marzo de 2020
#
# Descripción de Modo de uso:
#

import random
import math

#-------------------------------------------------------
#2 clases

class Carta:
    figura = None #str
    valor = None #int
    #Da el formato a las cartas, si el valor es 1 (As) lo convierte en 20.
    def __init__( self, figura, valor ):
        self.figura = figura
        self.valor = valor
        if( self.valor == 1 ):
            self.valor = 20
    
    def __str__( self ):
        #Muestra la carta individual, asigna String a numericos específicos, (1=as, 12=reina, etc.)
        if( self.valor == 20 ):
            self.valor = "As"
        elif( self.valor == 11 ):
            self.valor = "Paje"
        elif( self.valor == 12 ):
            self.valor = "Reina"
        elif( self.valor == 13 ):
            self.valor = "Rey"
        return ( "{} de {}".format( self.valor, self.figura ) )
        

class Baraja:
    dict_cartas = None #cara:valor
    lista_figuras = ["Corazones", "Pinos", "Tréboles", "Diamantes"]
    lista_cartas = None 
    lista_jugadores = None

    def __init__(self):
        self.lista_cartas = []
        self.lista_jugadores = []
        self.dict_cartas = dict()
        self.genera_deck()
        self.genera_dict()

    def genera_dict( self ):
        for valor in range (2, 10):
            self.dict_cartas[str(valor)] = valor
        self.dict_cartas["Paje"] = 11
        self.dict_cartas["Reina"] = 12
        self.dict_cartas["Rey"] = 13
        self.dict_cartas["As"] = 20

    def genera_deck( self ):
        # Crea una baraja utilizando un loop, ademas revuelve las cartas de la baraja
        for cara in self.lista_figuras:
            for valor in range( 1, 14 ): 
                self.lista_cartas.append( Carta( cara, valor ) )
        self.revolver()

    def revolver( self ):
        # Revuelve las cartas de la baraja utilizando el importe "random" para cambiar las posiciones de ciertas
        # cartas dentro de la baraja
        for i in range( len( self.lista_cartas )-1, 0, -1 ):
            r = random.randint( 0, i )
            self.lista_cartas[i], self.lista_cartas[r] = self.lista_cartas[r], self.lista_cartas[i]

    def genera_mano( self, numero ):
        # Genera una lista de cartas dependiendo del numero indicado
        mano = []
        if numero <= math.floor(52/len(self.lista_jugadores)):    
            for i in range( 1, numero+1 ):
                mano.append( self.lista_cartas.pop() )
        else:
            print("Se ha seleccionado un número de cartas para las cuales \n \
            no se puede repartir la mano equitativamente. \n \
            Se reducirá la cantidad de cartas al número máximo posible.")
            numero = math.floor(52/len(self.lista_jugadores))
            for i in range ( 1, numero+1 ):
                mano.append( self.lista_cartas.pop() )
        return mano

    def guarda_jugador( self, jugador ):
        lista_jugadores.append( jugador )

class Jugador:
    nombre = None #str
    mano = None #lista

    def __init__( self, nombre ):
        self.nombre = nombre

    def despliega_mano( self ):
        #Despliega la mano del jugador
        for carta in self.mano:
            print(carta)

#deck=Baraja()
#manita=deck.generaMano(5)
#alex = Jugador("alex")
#alex.despliegaMano(manita)


