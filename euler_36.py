

def double_base():
    million = range(1, 1000001)
    b_million = []
    for i in million:
        b_million.append(int(str(bin(i))[2:]))

    return b_million


def isPalindrome(number):
    number_str = str(number)
    index_b = 0
    index_e = len(number_str)-1
    max_index = len(number_str) / 2

    while index_b < max_index:
        if int(number_str[index_b]) != int(number_str[index_e]):
            return 0
        index_b += 1
        index_e -= 1
    return 1


def palindromes():
    palinlist = []
    for i in range(1, 1000001):
        if isPalindrome(i):
            palinlist.append(i)
    return palinlist

def b_palindromes(pals):
    b_pals = []
    for i in pals:
        b_num = int(str(bin(i))[2:])
        if isPalindrome(b_num):
            b_pals.append(i)
    return b_pals

pal = palindromes()
my_b = b_palindromes(pal)
sum(my_b) = 872187
