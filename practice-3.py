"""
***************************** EJERCICIO 3 *************************************
"""

#definimos una lista vacía, la cual llenaremos con diccionarios que serán los productos
#indice es el orden que ocupa en la lista el producto que estamos añadiendo en este momento
#restándole 1, para que la indexación funcione
#así mismo, cantidad_total va acumulando el valor total de los productos
lista, indice, cantidad_total = [], 0, 0

#el programa pregunra al usuario si quiere introducir más gastos
#el bucle while se ejecuta de forma reiterada siempre que la proposición que lo siga sea verdadera
#con esto aseguramos que el programa solo funciona si obtiene un si o un no
continuar = input("Quieres introducir más gastos (si/no): ")
while continuar != "si" and continuar != "no":
    continuar = input("Quieres introducir más gastos (si/no): ")

#cuando el programa obtiene su primer si se ejecuta lo que sigue:
while continuar == "si":
    #a la lista se le añade un diccionario vacío con el comando append sobre lista
    lista.append({})
    #se pregunta por el motivo del gasto y se introduce como elemento del diccionario recién añadido
    lista[indice]["motivo"] = input("Motivo del gasto: ")
    #ídem con el lugar y la cantidad
    lista[indice]["lugar"] = input("Lugar del gasto: ")
    lista[indice]["cantidad"] = float(input("Cantidad gastada: "))
    #se actualiza el índice para que la siguiente vez que se ejecute el bucle y se añada un
    #nuevo diccionario vacío, los elementos motivo, lugar, y gasto, se añadan a él
    indice += 1
    #de nuevo se solicita al usuario que decida si desea o no seguir introduciendo datos
    #el programa solo funciona si obtiene un si o un no
    continuar = input("Quieres introducir más gastos (si/no): ")
    while continuar != "si" and continuar != "no":
        continuar = input("Quieres introducir más gastos (si/no): ")

#cuando el programa recibe un no, el bucle acaba y se ejecuta lo que sigue:
#\n imprime un salto de línea. Añadimos contenido a la string usando +
print("\n" + "Gastos: ")

#el bucle for sirve para que la acción que contiene se ejecute una vez por cada elemento en
#un conjunto. En este caso, se ejecuta para cada diccionario de lista
for producto in lista:
    #creamos una string que da información sobre el motivo, lugar, y cantidad de una compra
    #llamando a los distintintos elementos o keys del diccionario, escritas entre corchetes
    print(producto["motivo"] + " en " + producto["lugar"] + " : " + str(producto["cantidad"]) + " euros")
    #actualizamos cantidad_total sumandole el precio del producto. Como este bucle se
    #ejectutará para cada producto, cantidad_total será la suma de todos los precios, como queríamos
    cantidad_total += producto["cantidad"]

#finalmente, imprimimos por pantalla una string que indica la cantidad total acumulada
print("Cantidad total: " + str(cantidad_total) + " euros")
