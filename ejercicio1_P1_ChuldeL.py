# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print ("Realizado por: Leslie Chulde")
print ("")
""" Para comentar se utilizan las comillas al inicio y final"""
print ("Consultando los tipos de valores:")
print ("")
print("El tipo de datos de 875 es:")
print(type(875)) 
print("El tipo de datos de 4.89 es:")
print(type(4.89))
""" Tanto los valores entetos como decimales se ingresan en los paréntesis de type para saber el tipo de dato que se tiene"""
print("El tipo de dato del texto: Now better than never es:")
print(type("Now is better than never"))
""" Para saber si la frase corresponde a un string se debe poner el texto entre comillas sino no funciona """
print("El tipo de datos de 1.32 es:")
print(type(1.32))
print("¿El valor 5+8i corresponde a un valor entero?")
print(isinstance(5+8j, int))
""" Phyton trabaja con la j para el caso de números complejos y no se coloca comilla en los paréntsis de la función insistance"""
print("¿El valor 8.2 corresponde a un valor entero?")
print(isinstance(8.2, int))
""" La función compara y arroja una salida de true or false en este caso es de False"""
print("¿El texto: Readability counts corresponde a un valor string?")
print(isinstance("Readability counts", str))
"""Para verificar si es un string el texto debe estar entre comillas y se debe colocar str no la palabra string"""