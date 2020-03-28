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
  ganador = None          #Ganador se asigna aquí
  mano_ganadora = -1      #Se compara la mano ganadora en este
  dict_ganador = None     #Con este se devuelve la mano del ganador
  carta_mas_alta = -1     #En caso de que no tengan pares ni tercias, se almacena aquí la carta más alta
  jg_cma = None           #Se almacena el jugador que tiene la carta más alta
  lista_empate = []       #En caso de empate se almacenan los jugadores con empate aquó
  cpg = 0                 #Almacena la cantidad de pares máxima
  ctg = 0                 #Almacena la cantidad de tercias máxima
  empate = False          #Boolean de si hay empate
  max_puntaje = 0         #Máximo puntaje alcanzado
  for jugador in jugadores:     #El proceso se hace por cada jugador
    print(jugador.nombre)
    print("------------")
    jugador.despliega_mano()    #Mostramos sus cartas
    suma_cartas = 0
    dict_mano = dict()
    for carta in jugador.mano:  #En un diccionario vamos poniendo cuántas de cada valor hay
      valor_carta = carta.valor
      if valor_carta in dict_mano:
        dict_mano[valor_carta] += 1
      else:
        dict_mano[valor_carta] = 1
    cuenta_pares = 0            #Cuenta local de pares y tercias en la mano de un jugador
    cuenta_tercias = 0        
    par_alto = 0                #Cuenta del par más alto de la mano de un jugador
    tercia_alta = 0             #Cuenta de la tercia más alta de la mano de un jugador
    suma_puntaje = 0            #Sumamos el puntaje del jugador
    for llave, valor in dict_mano.items():      #Por cada valor único en la mano del jugador...
      if valor == 2:                          #Si es un par...
        suma_cartas += 2                        #Tiene dos cartas
        suma_puntaje += llave*2                 #Sacamos el puntaje
        cuenta_pares += 1                       #Contamos que lleva un par
        if llave > par_alto:                    #Si es su par de valor más alto...
          par_alto = llave                      #Guárdalo
      if valor == 3:                          #Si es una tercia...
        suma_cartas += 3                        #Tiene tres cartas
        cuenta_tercias += 1                     #Contamos que lleva una tercia
        suma_puntaje += llave*3                 #Sacamos el puntaje
        if llave > tercia_alta:                 #Si es la tercia de valor más alto...
          tercia_alta = llave                   #Guárdalo
      if valor == 4:                          #Si son 4 del mismo valor...
        suma_cartas += 4                        #Tiene 4 cartas
        cuenta_pares += 2                       #Suma dos pares
        suma_puntaje += valor*4                 #Obtenemos su puntaje
        if llave > par_alto:                    #Si su llave es el par más alto...
          par_alto = llave                      #Guárdalo
    print("Puntaje: {} \n".format(suma_puntaje))
    if suma_cartas == mano_ganadora:            #Si la suma de cartas es igual a la mano ganadora...
      lista_empate.append( [jugador, par_alto, tercia_alta, dict_mano] )    #Vamos a compararlas, guardala en la lista
      empate = True                             #Hay un empate
    elif suma_cartas > mano_ganadora:         #Si la suma de cartas supera a la de la mano ganadora...
      ganador = jugador                       #Este es el que va ganando
      max_puntaje = suma_puntaje              #Su puntaje es el máximo hasta ahora
      lista_empate = [ [jugador, par_alto, tercia_alta, dict_mano] ]    #Reescribe la lista de empate empezando por este
      cpg = cuenta_pares                      #Aquí está su cuenta de pares
      ctg = cuenta_tercias                    #Aquí está su cuenta de tercias
      mano_ganadora = suma_cartas             #Su suma de cartas es la nueva ganadora
      dict_ganador = dict_mano                #Se elige comparar suma de cartas porque puede que su puntaje sea mayor pero dos pares siempre le ganan a una tercia, por ejemplo
      empate = False                          #Si antes había empate, ahora no.
  if empate == True:              #Si hay empate
    if mano_ganadora == 0:      #Y nadie va ganando...
      ganador = None            #Empate 
    else:                       #Si hay más de uno con matches
      ganador, dict_ganador = comparar_empates( lista_empate, cpg, ctg )   #Compara las matches.
  return ganador, dict_ganador

def comparar_empates( lista_empate, cpg, ctg ):
  par_alto = 0
  tercia_alta = 0
  ganador = None
  dict_ganador = None
  if cpg > ctg:           #Cantidad de Pares > Cantidad de Tercias? Tienen prioridad los pares
    for lista in lista_empate:
      if lista[1] > par_alto:
        par_alto = lista[1]
        ganador = lista[0]
        dict_ganador = lista[3]
  else:                  #Cantidad de Tercias >= Cantidad de Pares, tienen prioridad las tercias
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
    motivo = "Mejor suerte para la próxima!"
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
