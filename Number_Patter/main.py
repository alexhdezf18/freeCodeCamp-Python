def number_pattern(n):
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n < 1:
        return "Argument must be an integer greater than 0."

    list_of_numbers = []
    for i in range(1, n + 1):
        list_of_numbers.append(str(i))
        result = " ".join(list_of_numbers)
    return result