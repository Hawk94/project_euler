def word_form(number):
    """word_form(number) -> string

    Returns the word form of the number.
    >>> word_form(32)
    'thirty-two'
    >>> word_form(123)
    'one hundred twenty-three'
    The highest number it is capable of converting is:
        999,999,999,999,999,999,999,999,999,999,999"""

    ones = ("", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    tens = ("", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")
    teens = ("ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")
    levels = ("", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion", "nonillion")

    word = ""
    #number will now be the reverse of the string form of itself.
    num = reversed(str(number))
    number = ""
    for x in num:
        number += x
    del num
    if len(number) % 3 == 1: number += "0"
    x = 0
    for digit in number:
        if x % 3 == 0:
            word = levels[x / 3] + ", " + word
            n = int(digit)
        elif x % 3 == 1:
            if digit == "1":
                num = teens[n]
            else:
                num = tens[int(digit)]
                if n:
                    if num:
                        num += ones[n]
                    else:
                        num = ones[n]
            word = num + word
        elif x % 3 == 2:
            if digit != "0":
                word = ones[int(digit)] + "hundredand" + word


        x += 1
    return word.strip(", ")

def euler(number):
    letter_length = 0
    for i in range(1, number+1):
        letter_length += len(word_form(i))
    return letter_length
