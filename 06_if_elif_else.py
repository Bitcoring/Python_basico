# """
# IF / ELIF / ELSE
# control de condiciones
# """

# llueve = True

# if llueve:
#     print("cogeré el paraguas") 
# else:
#     print("iré a pasear")

# print("resto del codigo")    

# Lunes = False  #los lunes como pizza
# Jueves = True  # jueves paella 
# # y el resto del dia un bocadillo

# if Lunes:
#     print("toca pizza")
# elif Jueves:
#     print("toca paella")

# else: 
#     print("toca bocadillo")

#     # Ejercicio:
#      # preguintar la edad al usuario
#      # si tienes menos de 12 años -> eres un niño
#     #  si tienes menos de 18 eres un adolescente 
#     #  si tienes menos de 30 eres muy joven
#     #  si tienes menos de 40 eres joven pero menos
#     #  si tienes mas --> tu puedes con todo
    
#     # menos_de_18=False
#     # menos_de_12=False
#     # menos_de_30=False
#     # menos_de_40=True
#     # mas_de_40=False


# edad = input("¿Qué edad tienes?")
# edad = int(edad)

# # if edad < 12:
# #     print("eres un niño")
# # elif edad < 18:
# #     print("eres un adolescente ")
# # elif edad < 30:
# #     print("eres muy joven ")
# # else:
# #     print("tu puedes con todo ")
# puede = edad-18
# no_puede = 18-edad

# if edad < 0:
#     print("no me lo creo")
# elif edad < 18:
#     print(f"aún no puedes votar te faltan {no_puede} años ")
# elif edad <120:
#     print(f"puedes votar desde hace {puede} años")    
# else:
#     print("no me lo creo")   

# *************************************************************
# ***************************************************************    


#pedir al usuario un numero 
# pedir otro numero
# pedir que operacion matematica quiere hacer suma resta mul, div, exponen, div entera, modulo
# si no es ninguan de estas mostraremos un error
# si divide por 0 tambien error 
#si no son numeros le diremos que no se puede hacer
# debe quedar:
# escriba el primer numero -> 1
# escriba el segundo numero -> 3
# ¿què operacion quiere realizar? suma

# 1+3=4




# primer_numero=input("escriba el primer numero")
# segundo_numero=input("escriba el segundo numero")
# primer_numero=int(primer_numero)
# segundo_numero=int(segundo_numero)
# operacion=input("que operacion quieres realizar")

# if operacion == "suma":
#     resultado = primer_numero + segundo_numero
# elif operacion == "resta":
#     resultado = primer_numero - segundo_numero
# elif operacion == "multiplicacion":
#     resultado = primer_numero * segundo_numero
# elif operacion == "division":
#     resultado = primer_numero / segundo_numero
# elif operacion == "modulo":    resultado = primer_numero // segundo_nume
    
   


# Pedir un número y validarlo
def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Debes ingresar un número válido.")

# Pedir una operación válida
def pedir_operacion():
    operaciones_validas = ["suma", "resta", "multiplicación", "división", "módulo"]
    while True:
        operacion = input("Elige una operación (suma, resta, multiplicación, división, módulo): ").strip().lower()
        if operacion in operaciones_validas:
            return operacion
        print("Error: Ingresa una operación válida.")

# Realizar la operación
def calcular(num1, num2, operacion):
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicación":
        return num1 * num2
    elif operacion == "división":
        if num2 == 0:
            return "Error: No se puede dividir por cero."
        return num1 / num2
    elif operacion == "módulo":
        if num2 == 0:
            return "Error: No se puede calcular el módulo con cero."
        return num1 % num2

# Programa principal
num1 = pedir_numero("Ingresa el primer número: ")
num2 = pedir_numero("Ingresa el segundo número: ")
operacion = pedir_operacion()

resultado = calcular(num1, num2, operacion)
print(f"El resultado de la {operacion} es: {resultado}")




# -***************************************************************************
# ****************************************************************************


    
# num_1 = float(input( "ingresa_primer_numero"))

# if num_1.isalpha():

#     print("se puede hacer")
# else:
#      print("no se puede") 




