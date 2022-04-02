# el caso base seria [[]], ya que debo retornar todas las combinaciones posibles,
# por lo tanto se que tengo que devolver un array de combinaciones, donde cada combinacion
# tambien es un array


def all_construct(target_word, array, memo={}):
    if not len(target_word):
        return [[]]  # array de combinacinoes vacias

    combinations = []
    for word in array:
        if target_word.startswith(word):
            aux = all_construct(target_word[len(word) :], array, memo)
            if aux != None:
                # a cada combinacion le agrego esta palabra
                for arr in aux:
                    arr.insert(0, word)
                    combinations.append(arr)
    return combinations if len(combinations) else None


# print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(all_construct("abcdeeeef", ["ab", "abc", "cd", "def", "abcd", "eeee", "f"]))
# print(all_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# print(
#     all_construct(
#         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
#         ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee", "f"],
#     )
# ) tarda banda debido al time complexity (exponencial)

# el peor de los casos, como tengo que hacer busqueda recursiva y retornar TODAS las combinaciones
# el peor sera cuando tengo miles de combinaciones por todos lados
def all_construct_v2(target_word, array, memo={}):
    if not len(target_word):
        return [[]]  # array de combinacinoes vacias
    if target_word in memo:
        return memo[target_word]

    combinations = []
    for word in array:
        if target_word.startswith(word):
            aux = all_construct_v2(target_word[len(word) :], array, memo)
            if aux != None:
                # a cada combinacion le agrego esta palabra
                for arr in aux:
                    combinations.append([word] + arr[:])

    memo[target_word] = combinations[:] if len(combinations) else None
    print(memo)
    return memo[target_word]


print("Result:", all_construct_v2("abcd", ["ab", "abc", "cd", "def", "abcd"]))
print("Result:", all_construct_v2("purple", ["pu", "e", "rpl", "ple", "pur"]))
# print(
#     "Result:",
#     all_construct_v2("abcdeeeef", ["ab", "abc", "cd", "def", "abcd", "eeee", "f"]),
# )
# print(
#     "Result:",
#     all_construct_v2("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]),
# )
print(
    "Result:",
    all_construct_v2(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"],
    ),
)  # termina rapido

print(
    "Result:",
    all_construct_v2(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"],
    ),
)  # Este no termina nunca mas, por el problema que dije antes. Como tengo que devolver todas las combinaciones
# No termina mas de recorrer el arbol
# Recordemos que como maximo la altura del arbol sera m, siendo m la cantidad de caracteres de target_sum. Este caso se dara cuando saco
# caracter por caracter.
# Como si o si tengo que devolver todas las combinaciones posibles, y las mismas estaran en las hojas, el peor de los casos seria
# cuando todas las combinaciones generadas son combinaciones correctas, como lo es el caso de arriba (bueno todas todas no)
# Time complexity es exponencial.
