#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Carta:

	#Vamos a crear un metodo constructor que se encarga de definir los atributos
	def __init__(self, numeroDeCarta, colorCarta, simbolo):
		self.numero = numeroDeCarta
		self.color = colorCarta
		self.simbolo = simbolo


	def imprimir(self):
		print("La carta es: " + str(self.numero) + " de " + self.simbolo)


	def asignarNumero(self, valor):
		self.numero = valor






#Creacion de una instancia de la clase Carta
carta1 = Carta(4, "negro" , "espadas")
carta1.imprimir()

carta2 = Carta(3, "rojo" , "corazones")
carta2.imprimir()
carta2.asignarNumero(9)
carta2.imprimir()
#nombre de variable = nombre de la clase