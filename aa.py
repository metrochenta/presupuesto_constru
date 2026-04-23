import os
os.system("cls")

presupuesto_elevado = 1.10
IVA = 0.19 
presupuesto_maximo = 50000000 
nombre_proyecto = input("ingrese nombre del proyecto\n").title()

try:
    cantidad_metro2 = int(input("ingrese cantidad de metros cuadrados a construir\n"))
    costo_metro2 = int(input("ingrese el costo por metro cuadrado\n"))
    cantidad_trabajadores = int(input("ingrese cantidad de tabajadores\n"))
    pago_trabajador = int(input("ingrese el pago por cada trabajador\n"))

    if cantidad_metro2 > 0 and costo_metro2 > 0 and cantidad_trabajadores > 0 and pago_trabajador > 0:

        costo_materiales = cantidad_metro2 * costo_metro2
        costo_mano = cantidad_trabajadores * pago_trabajador
        costo_neto = costo_materiales + costo_mano
        valor_iva = costo_neto * IVA 
        costo_total = valor_iva + costo_neto
        ct_redondeado = round(costo_total, 2)

        if costo_total <= presupuesto_maximo:
            estado = "aprobado, esta dentro del presupuesto!"
        elif costo_total > presupuesto_maximo and costo_total <= presupuesto_elevado:
            estado = "aprobado, monto ajustado!"
        else:
            estado = "Desaprobado, fuera de presupuesto!"
    else:
        print("algun valor no fue escrito correctamente!")

except:
    print("algun valor esta erroneo")
print(f"//////")
print(f"nombre del proyecto: {nombre_proyecto}")
print(f"costo total: ${ct_redondeado}")
print(f"Estado del proyecto: {estado}")
print(f"//////")
