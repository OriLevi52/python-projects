def count_elements_in_tuples(list_of_tuples):
    result = {}
    for t in list_of_tuples:
        for element in t:
            if element in result:
                result[element] += 1
            else:
                result[element] = 1
    return result
data = [("wow", 2, 3), (2, "wow", 4), (1, 5, 4)]
print(count_elements_in_tuples(data))