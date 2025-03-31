import numpy as np

a = int(input("enter number a\n"))
b = int(input("enter number b\n"))

while (a > b):
    a = int(input("enter a number for a that is smaller than b\n"))
    b = int(input("enter a number for b that is larger than a\n"))


def f1(x):
    return (np.exp(x) + np.log(x))

def f2(x):
    return (np.arctan(x) - (x ** 2))

def f3(x):
    return (np.sin(x) / np.log(x))

def f4(x):
    return (np.log(np.cos(x)))

def roots(f, a, b):
    x = np.linspace(a, b, 3)
    y = f(x)
    if a == 0:
        a = 0.00000000001  # avoid div by 0
    if (f(a) <= 0 <= f((a + b) / 2) or f(a) >= 0 >= f((a + b) / 2) or f((a + b) / 2) <= 0 <= f(b) or f(
            (a + b) / 2) >= 0 >= f(b)):  # if findable by bisection
        for i in range(len(y)):
            if y[i] < 0.000000000000001 and y[i] > -0.000000000000001:
                return ("%.10f" % x[i])  # returns to 10 decimal places
        if y[0] < 0 and y[1] > 0 or y[0] > 0 and y[1] < 0:
            return roots(f, a, (a + b) / 2)
        elif y[1] < 0 and y[2] > 0 or y[1] > 0 and y[2] < 0:
            return roots(f, (a + b) / 2, b)
        else:
            return "no roots"
    else:
        return "root cannot be determined by bisection\n"

choice = input("f1, f2, f3, or f4?\n")

if (choice == "f1" or choice == "1"):
    print(roots(f1, a, b))
elif (choice == "f2" or choice == "2"):
    print(roots(f2, a, b))
elif (choice == "f3" or choice == "3"):
    print(roots(f3, a, b))
elif (choice == "f4" or choice == "4"):
    print(roots(f4, a, b))