#! /usr/bin/python3
import random

class Carta:
    #Les da el formato a las cartas, si el valor es 1 (O sea, un as) lo convierte en 20.
    def __init__(self, figura, valor):
        self.figura = figura
        self.valor = valor
        if(self.valor==1):
            self.valor=20

    def mostrar(self):
        # metodo que muestra la carta individual ademas de darle valores String a numericos especificos, (1=as, 12=reina, etc.)
        if (self.valor==20):
            self.valor="As"
        elif (self.valor==11):
            self.valor="Paje"
        elif (self.valor == 12):
            self.valor = "Reina"
        elif (self.valor == 13):
            self.valor = "Rey"
        print("{} de {}".format(self.valor, self.figura))

class Baraja:
    def __init__(self):
        self.cartas=[]
        self.generaDeck()

    def generaDeck(self):
        # Crea una baraja utilizando un loop, ademas revuelve las cartas de la baraja
        for cara in ["Espadas", "Treboles", "Diamantes", "Corazones"]:
            for valor in range(1,14):
                self.cartas.append(Carta(cara,valor))
        self.revolver()

    def mostrar(self):
        # metodo que muestra la baraja utilizando el metodo "mostrar()" de la clase "Cartas"
        for carta in self.cartas:
            carta.mostrar()

    def revolver(self):
        # Metodo que revuelve las cartas de la baraja utilizando el importe "random" para cambiar las posiciones de cierta
        # carta a otro dentro de la baraja
        for i in range(len(self.cartas)-1,0,-1):
            r=random.randint(0,i)
            self.cartas[i],self.cartas[r] = self.cartas[r],self.cartas[i]

    def generaMano(self,numero):
        # metodo que genera una lista de cartas dependiendo del numero indicado
        mano=[]
        for i in range(1,numero+1):
            mano.append(self.cartas.pop())
        return mano

deck=Baraja()
manita=deck.generaMano(5)

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre

    def despliegaMano(self,mano):
        #Despliega la mano del jugador
        for carta in mano:
            carta.mostrar()


alex = Jugador("alex")
alex.despliegaMano(manita)


