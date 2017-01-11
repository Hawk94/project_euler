def square_chain(x):
    square_result = 0
    my_string = str(x)
    for i in my_string:
        my_int = int(i)
        square_result += my_int**2
    return square_result

def square_loop(x):
    result = 89
    my_square = x
    while my_square != 89:
        my_square = square_chain(my_square)
        if my_square == 1:
            break
    return my_square

def euler():
    answer = []
    for i in range(1, 10000001):
        if square_loop(i) == 89:
            print(i)
            answer.append(i)
    return answer
