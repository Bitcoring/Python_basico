"""
EXCEPCIONES 
Son erroes que se introducen durante la ejecucion del programa y lo interrumpen


# """
# import os
# os.system("cls")

try:
    num = float(input("escribe un numero"))
    # print(1/0)
    # print("despues de la división por cero")
except ValueError:
    print("has de introducir un número") 
except ZeroDivisionError:
    print("No se puede dividir por cero") 
except:
    print("a ocurrdio un error")     





