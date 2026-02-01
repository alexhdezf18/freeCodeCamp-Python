def square_root_bisection(number, tolerance = 1e-7, maximum = 100):
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number
    
    low = 0
    high = max(1, number)
    root = None

    for i in range(maximum):
        mid = (low + high) / 2
        
        if (high - low) <= tolerance:
            root = mid
            break

        if mid**2 < number:
            low = mid
        else:
            high = mid

    if root is not None:
        print(f"The square root of {number} is approximately {root}")
        return root
    else:
        print(f"Failed to converge within {maximum} iterations")
        return None