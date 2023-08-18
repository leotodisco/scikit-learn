"""
    Aritmetica in bitwise.
"""


"""
    Parameters

    base : int, default=None
        è la base della potenza
    exponent : esponente
"""
def bitwise_power(base, exponent):
    result = 1

    base = int(base)
    exponent = int(exponent)

    while exponent != 0:
        if exponent & 1:  # controlla se l'ultimo bit di exponent è 1
            result *= base

        base *= base  # eleva base al quadrato
        exponent >>= 1  # shift logico verso destra di exponent

    return result

"""
    ALGORITMO DELLA ANCIENT EGYPTIAN MULTIPLICATION
"""
def bitwise_multiply(x, y):
    x = int(x)
    y = int(y)
    result = 0

    while y > 0:
        if y & 1:  # If the rightmost bit of y is set (y is odd)
            result += x
        x <<= 1  # Left shift x (equivalent to multiplying x by 2)
        y >>= 1  # Right shift y (equivalent to dividing y by 2)
    return result


def bitwise_sum(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    
    while num2 != 0:
        carry = num1 & num2
        num1 = num1 ^ num2
        num2 = carry << 1
    return num1



