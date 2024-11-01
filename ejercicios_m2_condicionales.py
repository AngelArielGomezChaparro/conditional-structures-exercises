#Escriba un programa que pida dos números enteros y que calcule la división, indicando si la división es exacta o no.
#El comando round redondeara hacia el entero mas cercano
#asi que para en ese caso toca importar la biblioteca con "import math" y luego el comando math.floor para redondear al numero entero menor
import math
numerador = float(input("ingrese el primer numero: "))
denominador = float(input("ingrese el segundo numero: "))
if denominador == 0:
        print (f"no se puede dividir por 0 ")

else:
        resultado = numerador / denominador
        residuo = numerador % denominador
        resultado1 = math.floor(resultado)
        if residuo == 0:
                print(f"""El resultado de la division es exacta
                numerador = {numerador}
                denominador = {denominador}
                cociente = {resultado1}
                residuo = {residuo} """)
        else:
                print(f"""El resultado de la division no es exacta
                numerador = {numerador}
                denominador = {denominador}
                cociente = {resultado1}
                residuo = {residuo} """)
                