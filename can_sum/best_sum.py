# En cada delegacion, me fijo si uno de esos caminos me llevo al resultado, y si es asi, retorno el mas corto
# La idea de subdividir el problema. La cantidad de soluciones que tenga mi problema, sera la suma
# de las soluciones de problemas mas pequeños.
# En este caso, si yo quiero ver cuantos suman 8, dado [2,3], puedo ver la combinacion para 6 y 5 y luego dividir esos tambien recursivamente
# Cada vez que tenga un nodo y me pueda mover hacia otros nodos, ahi debo ver lo que me retornan mis hijos.
# De esos agarro el array mas corto

# version poco eficiente
def best_sum(target_sum, array):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    # aca analizo cual me devuelve el camino mas corto y lo devuelvo.
    shortest = None
    for n in array:
        child = target_sum - n
        child_comb = best_sum(child, array)
        if child_comb != None:
            child_comb.append(n)
            if not shortest or len(child_comb) < len(shortest):
                shortest = child_comb
    return shortest


print(best_sum(8, [2, 3, 4, 25]))

# Version mejorada

memo = {}


def best_sum_v2(target_sum, array):
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    if target_sum in memo:
        return memo[target_sum]

    # aca analizo cual me devuelve el camino mas corto y lo devuelvo.
    shortest = None

    for n in array:
        child = target_sum - n
        child_comb = best_sum_v2(child, array)
        if child_comb != None:
            child_comb = child_comb + [n]
            # child_comb.append(n) # como tiene efecto de lado, me modificaba directamente el array del memo,
            # por eso no me daba
            if not shortest or len(child_comb) < len(shortest):
                shortest = child_comb
    memo[target_sum] = shortest
    return shortest


print(best_sum_v2(100, [1, 3, 5, 25]))  # deberia darme [25,25,25,25]
