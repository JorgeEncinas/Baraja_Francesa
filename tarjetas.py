#!/usr/bin/python3
# Integrantes del equipo:
#   Alcaraz Biebrich Manuel Alejandro
#   Encinas Alegre Jorge Carlos
#   Romero Andrade Paula Cristina
# Fecha: 20 de Marzo de 2020
#
# Descripción de Modo de uso:
#  
#  
#  
#  
#
# Llamar:
#   
#   
#   
#   

import argparse

#-------------------------------------------------------
#2 clases

class Jugador:
    nombre = None #str
    mano = None #Lista

    def __init__( self, nombre, mano ):
        self.nombre = nombre
        self.mano = mano

    def despliega_mano(self):
        print(mano)

class Carta:
    valor = None #int
    figura = None #str

    def __init__( self, valor, figura ):
        self.valor = valor
        self.figura = figura

    def __str__( self ):
    print(str(valor) + "-" + figura)

class Baraja:
    dict_cartas = None #diccionario de cartas (cara:valor)
    lista_figuras = None #lista de figuras
    lista_cartas = None #lista de cartas
    lista_jugadores = None #lista de jugadores

    def __init__( self ):
        dict_cartas = dict()
        #lista_figuras =
        #lista_cartas = 
        #lista_jugadores =

    def genera_mano( self ):

    def guarda_jugador( self ):






