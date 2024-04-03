#ejercicio 10
sueldo_basico = float(input("Ingrese sueldo basico: "))
antiguedad = int(input("Ingrese antiguedad: "))
estado_civil = int(input("Ingrese 1 si es soltero o 2 si es casado"))
if estado_civil == 1:
    importe = sueldo_basico + sueldo_basico*0.05*antiguedad
elif estado_civil == 2:
    importe = sueldo_basico + sueldo_basico*0.07*antiguedad
else:
    print("Solo puede ingresar 1 o 2")
jubilacion = importe - importe*0.11
obra_social = importe - importe*0.03
sindicato = importe - importe*0.03
sueldo_neto = importe - jubilacion - obra_social - sindicato
print("Sueldo basico: ", sueldo_basico "Antiguedad: ", antiguedad "Estado civil: ", estado_civil "Descuento jubilacion: ", jubilacion "Descuento obra social: ", obra_social "Descuento sindicato: ", sindicato)
print("Su sueldo neto es: ", sueldo_neto)