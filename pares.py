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
import math

#-------------------------------------------------------
#2 funciones

def generar_manos( jugadores, numero_cartas, baraja ):
  for nombre in jugadores:
    jugador = tarjetas.Jugador( nombre )
    jugador.mano = baraja.genera_mano( numero_cartas )
    baraja.guarda_jugador( jugador )

def comparar_manos( jugadores, dict_cartas ):
  ganador = "Algo está saliendo mal xd"
  mano_ganadora = -1
  for jugador in jugadores:
    print(jugador.nombre)
    print("------------")
    jugador.despliega_mano()
    print("\n")
    suma_cartas = 0
    dict_mano = dict()
    for carta in jugador.mano:
      valor_carta = carta.valor
      if valor_carta in dict_mano.keys():
        dict_mano[valor_carta] += 1
      else:
        dict_mano[valor_carta] = 1
    print(dict_mano)
    for llave, valor in dict_mano.items():
      if valor > 1 and valor < 4:
        suma_cartas += (llave*valor)
    print("{} \n".format(suma_cartas))
    if suma_cartas > mano_ganadora:
      ganador = jugador
      mano_ganadora = suma_cartas
  return ganador

def motivoVictoria(mano):
  '''Toma la mano ganadora y hace un diccionario de valores, el cual mostrara si se repitieron valores (para comprobar que haya pares) y al final regresa un string que revela el motivo por el que gano. Ej: "Gano con un par"'''
  motivo=""
  dv=dict()
  pares=0
  tercias=0
  p="pares"
  t="tercias"
  for carta in mano:
    if carta.valor in dv:
      dv[carta.valor]+=1
    else:
      dv[carta.valor]=1
  for k,v in dv.items():
    if v=2:
      pares+=1
    if v=3:
      tercias+=1
  if pares=1:
    p="par"
  if tercias=1:
    t="tercia"
  motivo="Gano con "+pares+" "+p+" y "+tercias+" "+t+"."
  return motivo

#-------------------------------------------------------
#3 ejecucion de main

def main( jugadores, numero_cartas ):
  baraja = tarjetas.Baraja()
  if numero_cartas > math.floor(52/(len(jugadores))):
    print("Se ha seleccionado un número de cartas para las cuales \n \
    no se puede repartir la mano equitativamente. \n \
    Se reducirá la cantidad de cartas al número máximo posible.")
    numero_cartas = math.floor(52/(len(jugadores)))
  humillar = False
  string_humillar = "AM: Eres patético, humano."
  if len( jugadores ) < 2:
    jugadores.append("AM")
    humillar = True
  generar_manos( jugadores, numero_cartas, baraja )
  ganador = comparar_manos( baraja.lista_jugadores, baraja.dict_cartas )
  print("El ganador es {}!".format(ganador.nombre))
  if humillar == True and ganador.nombre == "AM":
    print(string_humillar)
  print(motivoVictoria(ganador.mano))
  

if __name__=="__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-j','--jugador',dest='jugador',help="nombre del jugador", \
  	                  action="append", required=True)
  parser.add_argument('-m','--mano',dest='mano',help="cantidad de cartas en mano", required=False, default=5)
  args = parser.parse_args()
  jugadores = args.jugador
  numero_cartas = args.mano
  main( jugadores, numero_cartas )
