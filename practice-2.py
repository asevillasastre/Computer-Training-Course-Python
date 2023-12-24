"""
***************************** EJERCICIO 2 *************************************
"""

#primero pedimos al usuario que escribe el nombre del mes mediante el comando input
mes = input("Introduzca el nombre del mes: ")

#utilizamos la instrucción if para comrpobar si el nombre del mes introducido coincide con alguno conocido
#nótese que el programa no distingue entre meses con o sin mayúscula
#la instrucción or actúa como la unión lógica y el caracter reservado \ permite escribir en la siguente línea
if mes == "enero" or mes == "Enero" or \
mes == "marzo" or mes == "Marzo" or \
mes == "mayo" or mes == "Mayo" or \
mes == "julio" or mes == "Julio" or \
mes == "agosto" or mes == "Agosto" or \
mes == "octubre" or mes == "Octubre" or \
mes == "diciembre" or mes == "Diciembre":
    print(mes + " tiene 31 días")

#la instrucción elif se ejecuta si y solo si no se cumplen los requisitos del condicional anterior
#pero sí se cumple la proposición que lo sigue
#en el caso de Febrero, el mes NO es del conjunto anterior que tienen 31 días, pero SÍ es Febrero
#con lo que el elif se ejecuta
elif mes == "febrero" or mes == "Febrero":
    print(mes + " tiene 28 días")

elif mes == "abril" or mes == "Abril" or \
mes == "junio" or mes == "Junio" or \
mes == "septiembre" or mes == "Septiembre" or \
mes == "noviembre" or mes == "Noviembre":
    print(mes + " tiene 30 días")

#lo que sigue a una estructura else se ejecuta si y solamente si no se cumplen los requisitos del
#condicional que lo precede. Con esto, en caso de introducir un mes erróneo, el programa lo notifica
else:
    print("No conozco ese mes")
