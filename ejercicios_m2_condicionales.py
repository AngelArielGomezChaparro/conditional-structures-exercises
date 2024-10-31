#Escriba un programa que pida dos números enteros y que calcule la división, indicando si la división es exacta o no.

numerador = int(input("ingrese el primer numero: "))
denominador = int(input("ingrese el segundo numero: "))


if denominador == 0:
        print (f"no se puede dividir por 0 ")
else:
     resultado = numerador / denominador
     residuo = numerador % denominador
     resultado1 = round(resultado)
     if residuo == 0:
      print(f"""El resultado de la division es exacta
        numerador = {numerador}
        denominador = {denominador}  
        cociente = {resultado1}
        resto = {residuo} """)
     else:
        print(f"""El resultado de la division no es exacta
        numerador = {numerador}
        denominador = {denominador}  
        cociente = {resultado1}
        resto = {residuo} """)

