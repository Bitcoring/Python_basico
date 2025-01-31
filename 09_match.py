# """
# MATCH = SWITCH DE JS O JAVA

# """

# mes = "enero"

# match mes: 
#     case "enero":
#         print("iré a new york")
#     case "Febrero":
#         print("iré a paris")
#     case "marzo"| "abril" | "mayo":
#         print("iré a Londres")
#     case _ : # si no es ninguno de los casos entonces:
#         print("No sé a donde iré")       

# *********************************************************
# *********************************************************

# try:
#     num_1 = float(input("ingrese el primer número"))
#     num_2 = float(input("ingrese el segundo número"))

#     operación = input ("qué operaciòn quieres realizar")

#    match operación:
#          case "suma"
#          print(num_1 + num_2)

# ************************************************************
# ************************************************************


#EJERCICIO 

# Preguntar al usuario que día de la semana es ( lunes , martes, et c)
# lunes: toca sistemas
# martes, miercoles, jueves o viernes: " toca python"
# sabado o domingo: " es fin de semana"
# si dice otra cosa: "creo que estas confundido"


dia = input("qué día de la semana es").lower()

match dia:
    case "lunes":
     print("toca sistemas")
    case "martes" | "miercoles" | "jueves" | "viernes" :
     print("toca python")
    case "sabado" | "domingo":
     print("es fin de semana")
    case _ :
      print("creo que estás confundido")

**********************************************************************
***********************************************************************

