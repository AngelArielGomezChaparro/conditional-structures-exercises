
#  Cuando la Tierra completa una órbita alrededor del Sol, no han transcurrido exactamente 365 rotaciones sobre sí misma, sino un poco 
#  más. Más precisamente, la diferencia es de más o menos un cuarto de día.
#  Para evitar que las estaciones se desfasen con el calendario, el calendario juliano introdujo la regla de introducir un día adicional
#  en los años divisibles por 4 (llamados bisiestos), para tomar en consideración los cuatro cuartos de día acumulados.
#  Sin embargo, bajo esta regla sigue habiendo un desfase, que es de aproximadamente 3/400 de día.
#  para corregir este desfase, en el año 1582 el papa Gregorio XIII introdujo un nuevo calendario, en el que el último año de cada siglo 
#  dejaba de ser bisiesto, a no ser que fuera divisible por 400.
#  Escriba un programa que indique si un año es bisiesto o no, teniendo en cuenta cuál era el calendario vigente en ese año:



entrada = int(input("Escriba el año que desee saber que es bisiesto: "))

if entrada >= 1582:
    if (entrada % 4 == 0 and entrada % 100 != 0): 
     print(f"El año {entrada} es bisiesto. ")
    else:
       print(f"su año {entrada} no es bisiesto. ")
else:
    if entrada % 4 == 0:
            print(f"El año {entrada} es bisiesto.")
    else:
            print(f"El año {entrada} no es bisiesto.")
