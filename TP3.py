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
for i in range(0,5,1):
    pares=0
    nro=int(input("Ingresar numero: "))
    if nro%2==0:
        print("Par")
        pares= pares+1
    else:
        print("Impar")
print("Cantidad de numeros pares: ", pares)        