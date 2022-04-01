calculated_values = {}


def how_sum(target_sum, array, res=[]):
    if target_sum == 0:
        return res
    if target_sum < 0:
        return None
    if target_sum in calculated_values:
        return calculated_values[target_sum]

    for n in array:
        calculated_values[target_sum] = how_sum(target_sum - n, array, res + [n])
        if calculated_values[target_sum]:
            return calculated_values[target_sum]
    return []


# print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
# print(how_sum(7, [2, 4]))
# print(how_sum(8, [2, 3, 5]))
# print(how_sum(300, [7, 14])
