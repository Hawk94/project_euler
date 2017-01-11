import decimal

def champernowne():
    number_len = 0
    champer = []
    for i in range(1, 10000000):
        len_i = len(str(i))
        champer.append(i)
        number_len += i

    print(number_len)
    return champer

def c_number():
    c = champernowne()
    c_num = str()
    for i in c:
        c_num += str(i)
    c_num = c_num[:1000001]

    return c_num

def product(my_list):
    p = 1
    for i in my_list:
        p *= i
    return p

def euler():
    c = c_number()
    d_num = [1, 10, 100, 1000, 10000, 100000, 1000000]
    cd_num = []
    for i in d_num:
        cd_num.append(int(c[i-1]))
    decimal_num = []

    return cd_num
