

def n_digits(n):
    start = 1
    end = 10
    for i in range(n):
        start = start*10
        end = end*10

    return (start, end)

def n_digit_power(n):
    my_var = []
    for i in range(1, 100):
        if i == len(str(n**i)):
            my_var.append((n, i))
    return my_var

def euler():
    result = []
    for y in range(1, 1000):
        result.append(n_digit_power(y))
    return result
