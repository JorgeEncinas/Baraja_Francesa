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
import tarjetas

#-------------------------------------------------------
#2 funciones

def generar_manos( jugadores ):
  for nombre in jugadores:
    jugador = tarjetas.Jugador( nombre )
    jugador.mano = baraja.genera_mano
    baraja.guarda_jugador( jugador )

def obten_valor( carta, dict_cartas ):
  temp = carta.split("-")
  llave = temp[0]
  valor_carta = dict_cartas.get(llave)
  return valor_carta

def comparar_manos( jugadores, dict_cartas ):
  ganador = ""
  mano_ganadora = -1
  for jugador in jugadores:
    print(jugador.nombre)
    print("------------")
    jugador.despliega_mano()
    suma_cartas = 0
    for carta in jugador.mano:
      valor_carta = obten_valor( carta, dict_cartas )
      suma_cartas += valor_carta
    if suma_cartas > mano_ganadora:
      ganador = jugador.nombre
  return ganador

#-------------------------------------------------------
#3 ejecucion de main

def main( jugadores, numero_cartas ):
  baraja = tarjetas.Baraja()
  humillar = False
  string_humillar = "AM: Eres patético, humano."
  if len( jugadores ) < 2:
    jugadores.append("AM")
    humillar = True
  generar_manos( baraja.lista_jugadores )
  ganador = comparar_manos(baraja.lista_jugadores, baraja.dict_cartas )
  print(ganador)
  if humillar == True and ganador == "AM":
    print(string_humillar)
  

if __name__=="__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-j','--jugador',dest='jugador',help="nombre del jugador", \
  	                  action="append", required=True)
  parser.add_argument('-m','--mano',dest='mano',help="cantidad de cartas en mano", required=False, default=5)
  args = parser.parse_args()
  jugadores = args.jugador
  numero_cartas = args.mano
  main( jugadores, numero_cartas )