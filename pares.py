#!/usr/bin/python3
# Integrantes del equipo:
#   Alcaraz Biebrich Manuel Alejandro
#   Encinas Alegre Jorge Carlos
#   Romero Andrade Paula Cristina
# Fecha: 20 de Marzo de 2020
#
# Descripción de Modo de uso:
#  El programa reparte al azar la mano de los jugadores (al menos dos jugadores),
#  mostrando las cartas que obtuvo cada quien, así como el puntaje de cada uno
#  y muestra una leyenda con el nombre del jugador ganador y su puntuación.
#  El usuario jugará por lo menos contra la computadora para ver quién logra la mejor mano.
#  Para este juego solo valdrán los pares y los tríos de cartas.
#
# Llamar:
#   ./pares.py -j nombre_jugador_1 -j nombre_jugador_2 -m 5
#   -j
#   -m --> NO PUEDE SER MAYOR A 52 CARTAS

import argparse

#-------------------------------------------------------
#2 funciones

def main():
    return

#-------------------------------------------------------
#3 ejecucion de main

if __name__=="__main__":
  parser = argparse.ArgumentParser()

  parser.add_argument('-j','--jugador',dest='jugador',help="nombre del jugador", 
  	                   action="append", required=True)
  parser.add_argument('-m','--mano',dest='mano',help="archivo donde buscar", required=False, default=5)

  args=parser.parse_args()
  jugador=args.jugador
  mano=args.mano

  main(jugador, mano)