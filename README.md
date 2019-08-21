| Tamaño del repositorio        | Hits           | Lenguaje utilizado|
| ------------- |:-------------:| :-------------:| 
| ![GitHub repo size in bytes](https://img.shields.io/github/repo-size/jciccio/principios2-19.svg?style=for-the-badge)      | [![HitCount](http://hits.dwyl.com/jciccio/principios2-19.svg)](http://hits.dwyl.com/jciccio/principios2-19) | Python 3|
    
# Principios 2-19

## Material visto en clase
Ejemplos tomados del código fuente generado en las distintas lecciones.


1. Creación de objetos
  * Creación de clases (__class__)
  ```python
  class Carta: #Declaración de una clase, usando la palabra resevada class
  ```
  
  * Creación de variables de instancia (uso de __self__)
  ```python
  self.numero = 8 #Se crea un atributo numero usando la sintaxis self.X
  self.palo = "Corazones" #Se crea e inicializa el atributo palo
  ```
  
  * Generación de instancias ( __variable = NombreDeClase()__)
  ```python
  carta1 = Carta() #Ejemplo sin parámetros
  carta2 = Carta(7,'Corazones') #Ejemplo con parámetros
  ```
  
  * Creación de funciones en clases (acciones __def nombreMetodo(parámetros)__) básicas
  ```python
  def sumar(self, valor1, valor2):
     resultado = valor1 + valor2
     return resultado
  ``` 
  
2. Transformación de tipos de datos utilizando __casting__
```python
 float(), int(), str()
```

| Método        | Descripción           | Ejemplo
| ------------- |:-------------:| :-------------:|
| float()        | Conversión a número real  | float("12.4") --> 12.4
| int()        | Conversión a número entero  | int(12.4) --> 12
| str()        | Conversión a hilera de caracteres | str(12) --> "12"