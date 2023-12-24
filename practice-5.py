"""
***************************** EJERCICIO 5 *************************************
"""

def lee_fichero(fichero):
    """
    esta función devuelve una lista con los números presentes en un fichero
    """
    #usamos open para abrir el fichero dado, que asociamos a la variable abierto
    #así como una lista vacía que contendrá las cifras que obtengamos del fichero
    abierto, lista = open(fichero), []
    #para cada línea, la añadimos como int en vez de como str a la lista, usando int()
    for numero in abierto:
        lista.append(int(numero))
    #devolvemos la lista con todos los números
    return lista
    #finalmente cerramos el fichero
    abierto.close()

def solo_pares(lista):
    """
    esta función devuelve una lista que contiene los numeros pares presentes en otra dada
    """
    #acreasmo lista vacía que contendrá las cifras que comprobemos son pares
    result = []
    #para cada elemento, comprobamos si el número que contiene vale 0 en módulo 2,usando %
    #si efectivamente es par, la añadimos a result
    for numero in lista:
        if int(numero) % 2 == 0:
            result.append(int(numero))
    #devolvemos la lista con todos los números pares
    return result


def escribe_fichero(lista, fichero):
    """
    esta función escribe en un fichero una lista de números
    """
    #abrimos el fichero con "w", osea, para escribir en él, y lo asociamos a la variable abierto
    abierto = open(fichero, "w")
    #por cada elemento de la lista dada, añadimos la str que lo corresponde al fichero
    #así como un salto de línea, con \n
    for numero in lista:
        abierto.write(str(numero) + "\n")
    #ahora fichero contiene columnas con los números de lista
    #finalmente cerramos el fichero
    abierto.close()
