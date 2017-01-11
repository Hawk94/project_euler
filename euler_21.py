def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def amicable_number(number):
    factors_1 = sum(factors(number),-number)
    numbers_2 = sum(factors(factors_1),-factors_1)
    if number == numbers_2:
        amicable_num = (number, factors_1)
        return amicable_num
    else:
        return 0

def euler():
    amicables = []
    for i in range(2,10001):
        amicable = amicable_number(i)
        if amicable > 0:
            amicables.append(amicable)
    return amicables

my_euler = euler()
euler_sum = 0

for i in my_euler:
    for x in i:
        euler_sum += x[0]

summer = []
for i in my_euler:
    if i[0] != i[1]:
        summer.append(i[0])
