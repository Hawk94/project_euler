
def triangle_number(length):
    triangles = []
    natural_numbers = range(1,length)
    for i in natural_numbers:
        triangles.append(sum(natural_numbers[:i]))
    return triangles


def factors(number):
    list_divisors = []
    half = int(number/2)

    for i in range(1,half):
        if number % i == 0:
            list_divisors.append(i)


    print(len(list_divisors))


def euler():
    for i in triangle_number(10000):
        if len(test(i)) == 200:
            print(i)



def test(number):
    return set(reduce(list.__add__,([i, number/i] for i in range(1, int(number**0.5) + 1) if number % i == 0)))
