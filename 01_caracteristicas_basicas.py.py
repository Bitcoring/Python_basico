¨¨¨
CARACTERISTICAS BASICAS DE PYTHON
¨¨¨
# VARIABLES
# Una variable es un espacio en memoria para guardar datos
# por tanto es un contendor

# para crear una variable...
# identificador = valor 

# Hay reglas para llamar a los identificadores = nombre de la variable
# no se puede hacer:
#       1variable (empezar por un numero, despues si lo puede llevar)
#       $variable (ni empezar por simbolo especial)

# de estos errores nos avisara vsc

# No debemos hacer ( no son exactamente errores):

#     contener caracteres fuera del idioma ingles, como ñ, Ç, tildes, à,ò , etc
#     Empezar por guion bajo (determinado para determinadas situaciones)
#     Utilizar palabras reservadas

# que debemos hacer:

#    Nombrar a nuestras varaibles con palabras descriptivas
#    Podemos usar màs de una palabra separada por un guiòn bajo (directiva PEP-8)
#    Intentar que las lineas de codigo no sean muy largas

Las variables tienen tipo 
  -- (nùmeros) -> (int), decimales (float) , complejos
  --  texto -> strings
  -- booleans -> true/false
  -- 

PYTHON ES DE TIPADO DINAMICO 

numero = 1  ENTERO
numero = "uno" STRING

PYTHON ES DE TIPADO FUERTE

suma = numero + 2 darà error, pues no deja sumar numeros y letras

concatenacion = numero + str(2)
suma_numerica = int("1") + 2

eN PYTHON por defecto no existen las constantes
PI = 3.1416

