#ejercicio 10
sueldo_basico = float(input("Ingrese sueldo basico: "))
antiguedad = int(input("Ingrese antiguedad: "))
estado_civil = int(input("Ingrese 1 si es soltero o 2 si es casado: "))
if estado_civil == 1:
    importe = sueldo_basico + sueldo_basico*0.05*antiguedad
elif estado_civil == 2:
    importe = sueldo_basico + sueldo_basico*0.07*antiguedad
else:
    print("Solo puede ingresar 1 o 2")
jubilacion = importe*0.11
obra_social = importe*0.03
sindicato = importe*0.03
sueldo_neto = importe - jubilacion - obra_social - sindicato
print("Sueldo basico: ", sueldo_basico, "\nAntiguedad: ", antiguedad, "\nEstado civil: ", estado_civil, "\nDescuento jubilacion: ", jubilacion, "\nDescuento obra social: ", obra_social, "\nDescuento sindicato: ", sindicato)
print("Su sueldo neto es: ", sueldo_neto)

#ejercicio for in
pares=0
total=0
for i in range(0,5,1):
    nro=int(input("Ingresar numero: "))
    if nro%2==0:
        print("Par")
        pares = pares + 1
        total = total + nro
    else:
        print("Impar")
promedio=(total//pares)
print("Promedio de los numeros pares: ", promedio)
print("Cantidad de numeros pares: ", pares)

#ejercicio while
suma = 0
nro = int(input("Ingresar numero: "))
while nro >= 0:
    suma = suma + nro
    nro=int(input("Ingresar numero: "))
print("La suma es: ",suma)

#ejercicio while 2
total=0
pregunta = 0
temperaturas = int(input("Ingrese valor de temperatura, para finalizar ingrese 0: "))
while temperaturas != 0:
    pregunta = pregunta + 1
    total = total + temperaturas
    temperaturas = int(input("Ingrese valor de temperatura, para finalizar ingrese 0: "))
promedio = (total/pregunta)
print("El promedio de temperaturas es: ", promedio)