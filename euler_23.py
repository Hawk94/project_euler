def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

ceiling = 28123

def abundant_numbers(number):
    divisors = factors(number)
    summer = sum(divisors)-number
    if number < summer:
        return number
    return 0

def euler():
    abundant = []
    for i in range(1,28124):
        abundant.append(abundant_numbers(i))
    return abundant

euler_problem = euler()
eul = []
for i in euler_problem:
    if i > 0:
        eul.append(i)

eu = list(itertools.combinations_with_replacement(eul,2))

summer = []
for i in eul:
    if sum(i) < ceiling:
        summer.append(sum(i))

my_range = range(1,28124)
to_remove = set(summer)
not_sum_of_abundant = [x for x in my_range if x not in to_remove]
sum(not_sum_of_abundant) = 4179871
