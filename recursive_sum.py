def recursive_sum(array):
    if len(array) == 1:
        return array[0]
    else:
        return array[len(array)] + recursive_sum(array[1:])

arr = [1,2,3,4,5,6,7]
print(recursive_sum(arr))