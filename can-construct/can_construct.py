# Mismo aproach que el de la suma. Empiezo desde el target, y voy sacando ocurrencias de las palabras
# que haya en el array. Puedo sacar varias veces si es posible una ocurrencia de la palabra

# Si yo saco caracteres de la mitad por ejemplo, puede suceder que cree nuevas adyacencias que anteriormente no estaban
# Por eso como restriccion, solo se puede sacar del principio.


def can_construct(target_word, array):
    if not len(target_word):
        return True

    for word in array:
        len_word = len(word)
        if target_word.startswith(word) and can_construct(
            target_word[len_word:], array
        ):
            return True
    return False


# print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(can_construct("abcdeef", ["ab", "abc", "cd", "def", "abcd"]))
# print(can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
# print(
#     can_construct(
#         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
#         ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"],
#     )
# )  # este tarda infinitamente


def can_construct_v2(target_word, array, memo={}):
    if not len(target_word):
        return True
    if target_word in memo:
        return memo[target_word]

    for word in array:
        len_word = len(word)
        if target_word.startswith(word) and can_construct_v2(
            target_word[len_word:], array, memo
        ):
            memo[target_word] = True
            return True
    memo[target_word] = False
    return False


# print(can_construct_v2("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
# print(can_construct_v2("abcdeeeef", ["ab", "abc", "cd", "def", "abcd"]))
# print(can_construct_v2("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(
    can_construct_v2(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"],
    )
)
