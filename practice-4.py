"""
***************************** EJERCICIO 4 *************************************
"""

def tipo_triangulo(a, b, c):
    """
    esta función devuelve el tipo de triángulo que forman lados de longitud a, b, y c
    también indica si tales lados no pueden formar un triángulo
    """
    #si la suma de dos lados es mayor que el tercero no tenemos un triángulo
    if not (a + b > c and a + c > b and b + c > a):
        print("No es un triángulo")

    #si es un triángulo procedemos a la clasificación:
    #si los 3 lados son iguales, es equilátero
    elif a == b and a == c:
        print("Equilátero")

    #si todos son distintos, es escaleno
    elif a != b and a != c and b != c:
        print("Escaleno")

    #en caso contrario, 2 lados han de ser iguales entre sí, y distintos del tercero
    #con lo que el triángulo es isósceles
    else:
        print("Isósceles")
