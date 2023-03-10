

def remove_smallest(numbers):
    # raise NotImplementedError("TODO: remove_smallest")
    # m = min(numbers)
    m = min(numbers)
    while m in numbers:
        numbers.remove(m)
    return numbers

list_s = [1, 2, 3, 1, 1]
print(remove_smallest(list_s))