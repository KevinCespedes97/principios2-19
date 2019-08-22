#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Carta: #Declaración de una clase, usando la palabra reservada class

	
	#Los elementos indentados (con sangría a este nivel) serán parte de la clase

	#Constructor de clase, la acción __init__ es llamada sólo una vez
	#Cuando se crea una nueva instancia de la clase
	#Entre los paréntesis se definen las variables que se desean recibir al
	#Crear un objeto y usarlas para dar valor a los atributos
	def __init__(self, numeroDeCarta, colorCarta, simbolo):
		#Los elementos con sangría a este nivel serán parte del método __init__
		self.numero = numeroDeCarta #Se crea un atributo numero usando la sintaxis self.X
		self.color = colorCarta #Se crea e inicializa el atributo color
		self.simbolo = simbolo


	def imprimir(self):
		print("La carta es: " + str(self.numero) + " de " + self.simbolo)
		#Recuerde que para concatenar (unir) Strings, todos los elementos
    	#Deben ser del mismo tipo por lo que convertimos el numero en un String


	def asignarNumero(self, valor):
		self.numero = valor

	#En algunas ocasiones, queremos que los métodos retornen un valor.
	#Por ejemplo el siguiente metodo retorna el valor de un numero
	#Para retornar, se utiliza la palabra reservada return seguido de lo que queremos retornar
	def obtenerNumero(self):
		return self.numero






#Creacion de instancias de la clase Carta
#Note que esto no es parte de la clase, por tanto la indentación (Sangría)
#Vuelve a la izquierda
carta1 = Carta(4, "negro" , "espadas")
carta1.imprimir()

carta2 = Carta(3, "rojo" , "corazones")
carta2.imprimir()
#Para una instancia existente, se pueden sobreescribir los valores de los atributos:
carta2.asignarNumero(9)
carta2.imprimir()
#nombre de variable = nombre de la clase
valorDeLaCarta2 = carta2.obtenerNumero()
print("El numero de la instancia carta2 es: " + str(valorDeLaCarta2))