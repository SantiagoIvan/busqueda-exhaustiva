def count_construct(target_word, array, memo={}):
    if not len(target_word):
        return 1
    if target_word in memo:
        return memo[target_word]

    count = 0
    for word in array:
        if target_word.startswith(word):
            aux = count_construct(target_word[len(word) :], array, memo)
            count += aux
    memo[target_word] = count
    return count


print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"], {}))
print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef"], {}))
print(count_construct("abcdeeeef", ["ab", "abc", "cd", "def", "abcd"], {}))
print(count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], {}))
print(
    count_construct(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee", "eeeeeee"],
        {},
    )
)
print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"], {}))
print(
    count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], {})
)
