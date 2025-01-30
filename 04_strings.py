# """
# CADENAS DE TEXTO  =>  Strings

# """

# string_1 = 'hola'

# string_2 = "hola"

# string_3 = """hola"""

# nombre = "Hammer"

# apellido = "arandia"

# edad = 35

# print(f"hola me llamo {nombre} {apellido} y tengo {edad} años")

# nombre = input("Escribe tu nombre -> ")
# print(nombre)

frase = "manzana podrida"

# Primer caracter del string

print("whatever>", frase[0])

print("frase[0:7]", frase[0:7])

# caracteres en posicion par
# frase[::2]
print("frase[::2]", frase[::2])

# cuantos caracteres hay en el string
print("len(frase)", len(frase))

#convertir el texto en mayuscula

print(frase.upper())

#dejarlo, convertirlo del todo a mayusculas

frase=frase.upper()

print(frase)

#dejarlo, convertirlo del todo a minusculas

frase=frase.lower()

print(frase)

#Empezar el string con mayuscula

print(frase.capitalize())

# Invertir mayusculas y minusculas

print(frase.swapcase())

# contar caracteres


print("frase.count ('a') => ", frase.count("a"))

# Encontrar la posicion de un caracter o grupo de caracteres

print("frase.find ('a') => ", frase.find("m"))

# verificar si el texto empieza por ceirto caracter o grupo de caracteres, como es una pregunta me devolvera un bollean

print(frase.startswith("man"))

print(frase.startswith("zab"))

# verificar si el texto acaba por ceirto caracter o grupo de caracteres, como es una pregunta me devolvera un bollean

print(frase.endswith("ida"))

print(frase.endswith("man"))

# verificar si el texto es convertible a numero

numero = "10"
print(int(numero))
print(numero.isnumeric()) # verifica si es solo numero
print(numero.isalpha()) # verifica si es solo texto
print(numero.isalnum()) # verifica si texto y numero

# Cambiar caracteres
print(frase.replace("a","i"))

palabras_en_frase = frase.split(" ")

print(palabras_en_frase)

# Mini ejercicio

texto = "bUeNos dÌAs"  # Buenos dias

texto=texto.lower().capitalize()
print(texto)

