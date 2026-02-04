def quick_sort(array):
    less = []
    greater = []
    equal = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        result = quick_sort(less) + equal + quick_sort(greater)
        return result
    else:
        return array