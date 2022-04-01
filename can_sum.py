# Por cada valor del array me deberia generar un arbol con m aristas, siendo m la cantidad de elementos
# del array
# Esto es porque un nodo se va a poder relacionar con m elementos.
# La relacion sera la suma
# Deberia cortar la recursion cuando la suma sea mayor al target. De esa forma me quedan esas hojas anuladas

# Otra forma mucho mas facil es pensarlo al reves. Empiezo desde el target sum, ese seria mi root.
# Cada relacion ahora seria una resta con un elemento del array

# Time complexity: orden de complejidad: n cantida de elementos del array, m = target_sum; O(n) = n ** m
# Como en cada nivel, voy a tener tantas ramas como elementos en el array tenga, n es la base.
# Elevado a la m porque en el peor de los casos, tengo m niveles, suponiendo por ejemplo que voy restando de a 1.

calculated_values = {}

# funciona pero es poco eficiente
def can_sum(target_sum, array):
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    for n in array:
        if can_sum(target_sum - n, array):
            return True
    return False


calculated_values = {}

# Cual es la nueva complejidad de este algoritmo?
# Al memorizar resultados, estamos evitando esa repeticion de calculos que haciamos.
# (Se entiende mejor haciendo el dibujo del arbol)
# Va a haber muchos subarboles que van a querer resolver lo mismo. ¿can_sum(target_sum, array)?
# El array es fijo, lo que va a varias es el target_sum. Como voy restando, puede darse que a cierto numero
# llegue de maneras diferentes. En el grafo, puedo observar que estos subarboles seran identicos, por lo que
# no es necesario recalcularlos.
# Por eso se reduce a n * m, no vas a reexplorar subarboles.


def can_sum_v2(target_sum, array):
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    if target_sum in calculated_values:
        return calculated_values[target_sum]

    for n in array:
        calculated_values[target_sum] = can_sum_v2(target_sum - n, array)
        if calculated_values[target_sum]:
            return True
    return False


print(can_sum_v2(350, [7, 14]))
