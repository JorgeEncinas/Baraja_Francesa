# Baraja_Francesa
Juego de Baraja Francesa en Python

El siguiente programa a realizar, es un juego de baraja francesa, donde el usuario jugará contra la computadora para ver quién logra la mejor mano. Para este juego solo valdrán los pares y los tríos de cartas. El usuario iniciará el programa con el siguiente comando:

   ./pares.py -j nombre_de_jugador -j otro_jugador -m 5

Y el programa repartirá al azar la mano del jugador y la del al menos otro jugador, mostrando las cartas que obtuvo cada quién (con su nombre en la parte superior de la "mano"), así como el puntaje de cada uno y deberá mostrar una leyenda con el nombre del jugador ganador y su puntuación. La opción -m indica el número de cartas a repartir en la "mano". (Incluyan un filtro para no pasar de repartir 52 cartas!):

   ./pares.py -j yo -j tu -m 5
   
yo 
---------- 
10-P 
3-P 
4-T 
7-P 
K-C
   
tu 
---------- 
10-C 
2-T 
4-D 
5-D 
5-T

jugador: tu gano con 1 par

Muy importante: un par de 10s le gana a un par de 5s. Dos pares le ganan a 1 par.

La baraja francesa consta de 52 cartas distribuidas en 4 palos (corazones, diamantes, picas y tréboles), estos palos o conjuntos están conformados así: 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack (paje), Queen (reina), King (rey) y Ace (as).  Para este ejercicio, Jack tendrá un valor de 11, Queen 12, King 13 y Ace 20.

Es necesario hacer un archivo tarjetas.py el cual contendrá 3 clases:

Jugador 
(atributos: nombre (str), mano (lista) ) 
(métodos: __init__, despliega_mano() )

Carta 
(atributos: valor (int), figura (str)) 
(métodos: __init__, __str__ )

Baraja 
(atributos: diccionario de cartas ( cara:valor ), figuras (Corazones, Pinos, Tréboles, Diamantes), lista de cartas (52 en total), lista de jugadores) 
(métodos: __init__, genera_mano, guarda_jugador)

También es necesario el archivo pares.py, que importará la librería tarjetas.py.

![Criterios de Evaluacion](/Criterios_evaluacion/Criterios_de_evaluacion_BF.png)

![Criterios de Evaluacion_2](/Criterios_evaluacion/criterios-2.png)

![Criterios de Evaluacion_3](/Criterios_evaluacion/criterios-3.png)
