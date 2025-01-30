"""
IF / ELIF / ELSE
control de condiciones
"""

llueve = True

if llueve:
    print("cogeré el paraguas") 
else:
    print("iré a pasear")

print("resto del codigo")    

Lunes = False  #los lunes como pizza
Jueves = True  # jueves paella 
# y el resto del dia un bocadillo

if Lunes:
    print("toca pizza")
elif Jueves:
    print("toca paella")

else: 
    print("toca bocadillo")

    # Ejercicio:
     # preguintar la edad al usuario
     # si tienes menos de 12 años -> eres un niño
    #  si tienes menos de 18 eres un adolescente 
    #  si tienes menos de 30 eres muy joven
    #  si tienes menos de 40 eres joven pero menos
    #  si tienes mas --> tu puedes con todo
    
    # menos_de_18=False
    # menos_de_12=False
    # menos_de_30=False
    # menos_de_40=True
    # mas_de_40=False


edad = input("¿Qué edad tienes?")
edad = int(edad)

# if edad < 12:
#     print("eres un niño")
# elif edad < 18:
#     print("eres un adolescente ")
# elif edad < 30:
#     print("eres muy joven ")
# else:
#     print("tu puedes con todo ")
puede = edad-18
no_puede = 18-edad

if edad < 0:
    print("no me lo creo")
elif edad < 18:
    print(f"aún no puedes votar te faltan {no_puede} años ")
elif edad <120:
    print(f"puedes votar desde hace {puede} años")    
else:
    print("no me lo creo")   








    




