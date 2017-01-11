from __future__ import division
import decimal

def increasing_number(x):
    increasing = False
    string_number = str(x)
    string_comprehension = [i for i in range(1,len(string_number)) if int(string_number[i]) >= int(string_number[i-1])]
    if len(string_comprehension) == (len(string_number)-1):
        increasing = True
    return increasing

def decreasing_number(x):
    decreasing = False
    string_number = str(x)
    string_comprehension = [i for i in range(len(string_number)-1) if int(string_number[i]) >= int(string_number[i+1])]
    if len(string_comprehension) == (len(string_number)-1):
        decreasing = True
    return decreasing

def bouncy_number(x):
    if not increasing_number(x):
        if not decreasing_number(x):
            return x

def bouncy_percentage(bounce_range):
    bouncy = []
    for i in range(1,bounce_range+1):
        if bouncy_number(i) > 0:
            bouncy.append(i)
    return len(bouncy)/bounce_range


def bouncy_number_lists(bounce_range):
    bouncy = []
    for i in range(1,bounce_range+1):
        bouncy.append((i,bouncy_number(i)))
    return bouncy


def bouncy_number_lists(bounce_range):
    bouncy = []
    for i in range(1,bounce_range+1):
        if not bouncy_number(i):
            bouncy.append(i)
    return bouncy


0.9890000
0.499
1409000

summer = 0
percentage = 0
for i in bounce:
    percentage = summer/i[0]
    if i[1]:
        summer += 1
    if percentage > 0.9889:
        break
    print(i,percentage)

def euler():
    bouncy = 0
    number = 256000
    while bouncy < 0.99:
        bouncy = bouncy_percentage(number)
        number += 1
    print number
