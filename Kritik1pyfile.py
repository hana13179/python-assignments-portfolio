def arctan_series(x, n):
    result = 0.0  # Initializing Result
    for i in range(n):  # Sigma function
        term = (((-1) ** (i)) * ((x) ** (2 * i + 1))) / (2 * i + 1)
        # term = ((-1)i)*(x  (2 * i + 1)) / (2 * i + 1)
        result += term
    return result


def arctan_error_bound(x, n):
    # Returns the maximum error of the arctan_series approximation
    error = (x ** (2 * n + 1)) / (2 * n + 1)
    return error

    # retun abs ((x** (2 * n + 1))/ (2 * n + 1))


def arctan_function(x):
    is_error_bounded = False  # Boolean to determine if the function is bounded by an error.
    n = 1  # Start with a linear approximation and then add degrees afterwards.

    if x > 1 or x < 0:
        return "Error! variable x is out of the accepted range!"

    while is_error_bounded == False:
        error_bound = arctan_error_bound(x, n)  # Grab the amount from the function.

        if (error_bound <= 0.0001):
            is_error_bounded = True

        else:  # If the error is greater than, refine n by adding a degree to the polynomial.
            n += 1

    # Once the code exits the while loop, a valid degree of n has been achieved such that
    # The error will be less than 0.0001. So, we can use that n.

    a = arctan_series(x, n)

    return (a, n, error_bound)


print("Result for a = -1 is:", arctan_function(-1))
print("Result for a = 0 is:", arctan_function(0))
print("Result for a = 0.25 is:", arctan_function(0.25))
print("Result for a = 0.5 is:", arctan_function(0.5))
print("Result for a = 0.75 is:", arctan_function(0.75))
print("Result for a = 1 is:", arctan_function(1))








