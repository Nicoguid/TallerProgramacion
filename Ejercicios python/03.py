def programa():
    lado_1 = input("Ingrese lado 1: ")
    lado_2 = input("Ingrese lado 2: ")
    perimetro = (lado_1)* 2 + (lado_2)* 2
    area = (lado_1)*(lado_2)
    print("Perimetro: ", perimetro)
    print("Area: ", area)

programa()


def programa_2():
    numero = input("Ingrese numero: ")
    parte_entera = int(numero)
    parte_fraccionaria = numero - parte_fraccionaria
    print("Parte entera: ", parte_entera)
    print("Parte fraccionaria", parte_fraccionaria)

programa_2()

def programa_3():
    resultado = []
    for digito in str(numero):
        digito_cuadrado = int(digito)** 2
    resultado.append(str(digito_cuadrado))
    numero = int(input("Ingrese un numero de 5 digitos: "))
    if len(numero) != 5:
        print("Ingrese un numero natural de 5 digitos.")
    else:
        #no terminado

def programa_4():
    base = float(input("Ingrese base: "))
    altura = float(input("Ingrese altura: "))
    area = base * altura
    perimetro = (base)* 2 + (altura)* 2
    print("Calculos para un triangulo de base", base "y altura", altura)
    print("<<< Area= ", "{:.2f}".format(area) ">>>   <<< Perimetro= ", "{:.2f}".format(perimetro))

programa_4()

def programa_5():
    numero_decimal =  int(input("Ingrese un numero decimal (maximo 5 cifras)"))
    numero_octal = 
    if len(numero_decimal) != 5:
        print("Ingrese un numero natural de 5 digitos.")
    else:
        print("El numero en octal es: ", numero_octal)

programa_5()