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
  ganador = None
  mano_ganadora = -1
  dict_ganador = None
  carta_mas_alta = -1
  jg_cma = None
  lista_empate = []
  cpg = 0
  ctg = 0
  empate = False
  max_puntaje = 0
  for jugador in jugadores:
    print(jugador.nombre)
    print("------------")
    jugador.despliega_mano()
    print("\n")
    suma_cartas = 0
    dict_mano = dict()
    for carta in jugador.mano:
      valor_carta = carta.valor
      if valor_carta in dict_mano:
        dict_mano[valor_carta] += 1
      else:
        dict_mano[valor_carta] = 1
    print(dict_mano)
    cuenta_pares = 0
    cuenta_tercias = 0
    par_alto = 0
    tercia_alta = 0
    suma_puntaje = 0
    for llave, valor in dict_mano.items():
      if valor == 2:
        suma_cartas += 2
        suma_puntaje += llave*2
        cuenta_pares += 1
        if llave > par_alto: 
          par_alto = llave
      if valor == 3:
        suma_cartas += 3
        cuenta_tercias += 1
        suma_puntaje += llave*3
        if llave > tercia_alta: 
          tercia_alta = llave
      if valor == 4:
        suma_cartas += 4
        cuenta_pares += 2
        suma_puntaje += valor*4
        if llave > par_alto: 
          par_alto = llave
      if llave > carta_mas_alta:
        carta_mas_alta = llave
        jg_cma = jugador
        dict_ganador = dict_mano
    print("Puntaje: {} \n".format(suma_puntaje))
    if suma_cartas == mano_ganadora:
      lista_empate.append( [jugador, par_alto, tercia_alta, dict_mano] )
      empate = True
    elif suma_cartas > mano_ganadora:
      ganador = jugador
      max_puntaje = suma_puntaje
      lista_empate = [ [jugador, par_alto, tercia_alta, dict_mano] ]
      cpg = cuenta_pares
      ctg = cuenta_tercias
      mano_ganadora = suma_cartas
      dict_ganador = dict_mano
      empate = False
  if empate == True:
    if mano_ganadora == 0:
      ganador = jg_cma
    else:
      ganador, dict_ganador = comparar_empates( lista_empate, cpg, ctg )
  return ganador, dict_ganador

def comparar_empates( lista_empate, cpg, ctg ):
  par_alto = 0
  tercia_alta = 0
  ganador = None
  dict_ganador = None
  if cpg > ctg:
    for lista in lista_empate:
      if lista[1] > par_alto:
        par_alto = lista[1]
        ganador = lista[0]
        dict_ganador = lista[3]
  else:
    for lista in lista_empate:
      if lista[2] > tercia_alta:
        tercia_alta = lista[1]
        ganador = lista[0]
        dict_ganador = lista[3]
  return ganador, dict_ganador

def motivoVictoria( dt ):
  '''Toma la mano ganadora y regresa un string que revela el motivo por el que gano. Ej: "Gano con un par"'''
  motivo=""
  pares=0
  tercias=0
  cma = 0
  p="pares"
  t="tercias"
  for k,v in dt.items():
    if v==2:
      pares+=1
    if v==3:
      tercias+=1
    if k > cma:
      cma = k
  if pares==1:
    p="par"
  if tercias==1:
    t="tercia"
  if pares == 0 and tercias == 0:
    motivo = "Ganó por su carta más alta: {}".format(cma)
  else:
    motivo = "Ganó con {} {} y {} {}.".format(pares, p, tercias, t) 
  return motivo

#-------------------------------------------------------
#3 ejecucion de main

def main( jugadores, numero_cartas ):
  baraja = tarjetas.Baraja()
  humillar = False
  string_humillar = "AM: Eres patético, humano."
  if len( jugadores ) < 2:
    jugadores.append("AM")
    humillar = True
  if numero_cartas > math.floor(52/(len(jugadores))):
    print("Se ha seleccionado un número de cartas para las cuales \n \
    no se puede repartir la mano equitativamente. \n \
    Se reducirá la cantidad de cartas al número máximo posible.")
    numero_cartas = math.floor(52/(len(jugadores)))
  generar_manos( jugadores, numero_cartas, baraja )
  ganador, dict_ganador = comparar_manos( baraja.lista_jugadores, baraja.dict_cartas )
  if ganador is None:
    print("Empate")
  else:
    print("El ganador es {}!".format(ganador.nombre))
    print(motivoVictoria(dict_ganador))
    if humillar == True and ganador.nombre == "AM":
      print(string_humillar)
  
  

if __name__=="__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-j','--jugador',dest='jugador',help="nombre del jugador", \
  	                  action="append", required=True)
  parser.add_argument('-m','--mano',dest='mano',help="cantidad de cartas en mano", type=int, required=False, default=5)
  args = parser.parse_args()
  jugadores = args.jugador
  numero_cartas = args.mano
  main( jugadores, numero_cartas )
