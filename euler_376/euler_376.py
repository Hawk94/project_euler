"""How many sets of nontransitive dice exist for N = 30 ?."""

import itertools

generator = itertools.combinations(itertools.combinations_with_replacement(range(1,8), 6), 3)
returns =  [(1, 1, 1, 1, 1, 1), (1, 1, 1, 1, 1, 2), (1, 1, 1, 1, 1, 3)]

[ """""" for n in itertools.combinations(itertools.combinations_with_replacement(range(1,8), 6), 3)]


y for y in itertools.permutations(returns, 2)

this_list = [((1, 1, 1, 1, 1, 1), (1, 1, 1, 1, 1, 2)), ((1, 1, 1, 1, 1, 1), (1, 1, 1, 1, 1, 3)), ((1, 1, 1, 1, 1, 2), (1, 1, 1, 1, 1, 1)), ((1, 1, 1, 1, 1, 2), (1, 1, 1, 1, 1, 3)), ((1, 1, 1, 1, 1, 3), (1, 1, 1, 1, 1, 1)), ((1, 1, 1, 1, 1, 3), (1, 1, 1, 1, 1, 2))]


for generator in generators:

def time_me():
    generator_count = 0
    for play in range(6):
        game_count = 0
        game = [zip(itertools.repeat(x),generator[play][1]) for x in generator[play][0]]
        game_count = sum([max(i)>i[0] for i in game[0]])
        if game_count > 3:
            generator_count += 1
    if generator_count > 2:
        nontransitve_set += 1
    return generator_count

"""This List Comprehension will return a list of 6 possible games for each set of 3 dice"""

generators = (itertools.permutations(n, 2) for n in itertools.combinations(itertools.combinations_with_replacement(range(1,8), 6), 3))

"""Possible rule: All dice must sum to the same value?? Otherwise cannot be Nontransitive?"""

def get_all_equal_sets():
equal_sets = []
generator = list(itertools.combinations(itertools.combinations_with_replacement(range(1,8), 6), 3))
for i in generator:
    if sum(i[0])==sum(i[1])==sum(i[2]):
        equal_sets.append(i)

nontransitive_set = []

"""make the below function a generator. If it reaches > 108 failiures break."""

(for i in range(2))
for a_set in generator:
    rolls = []
dice_1 = a_set[0]
dice_2 = a_set[1]
dice_3 = a_set[2]
    rolls = rolls + [zip(itertools.repeat(x), dice_1) for x in dice_2]
    rolls = rolls + [zip(itertools.repeat(x), dice_1) for x in dice_3]
    rolls = rolls + [zip(itertools.repeat(x), dice_2) for x in dice_1]
    rolls = rolls + [zip(itertools.repeat(x), dice_2) for x in dice_3]
    rolls = rolls + [zip(itertools.repeat(x), dice_3) for x in dice_1]
    rolls = rolls + [zip(itertools.repeat(x), dice_3) for x in dice_2]
    rolls = [item for sublist in rolls for item in sublist]
    if sum([max(i)>i[0] for i in rolls]) > 107:
        nontransitive_set.append(a_set)

"""GENERATOR TO GENERATE 216 ROLLS IN A SET"""

for a_set in generator:
    rolls = (item for sublist in [zip(itertools.repeat(x), a_set[0]) for x in a_set[1]]+[zip(itertools.repeat(x), a_set[0]) for x in a_set[2]]+[zip(itertools.repeat(x), a_set[1]) for x in a_set[0]]+[zip(itertools.repeat(x), a_set[1]) for x in a_set[2]]+[zip(itertools.repeat(x), a_set[2]) for x in a_set[0]]+[zip(itertools.repeat(x), a_set[2]) for x in a_set[1]] for item in sublist)
    win = sum([max(i)>i[0] for i in rolls])
    wins.append(win)
    print(win)

generator = itertools.combinations(itertools.combinations_with_replacement(range(1,8), 6), 3)

roll_generator = [item for sublist in [zip(itertools.repeat(x), a_set[0]) for x in a_set[1]]+[zip(itertools.repeat(x), a_set[0]) for x in a_set[2]]+[zip(itertools.repeat(x), a_set[1]) for x in a_set[0]]+[zip(itertools.repeat(x), a_set[1]) for x in a_set[2]]+[zip(itertools.repeat(x), a_set[2]) for x in a_set[0]]+[zip(itertools.repeat(x), a_set[2]) for x in a_set[1]] for item in sublist for a_set in itertools.combinations(itertools.combinations_with_replacement(range(1,8), 6), 3)]

_____________________________________________________________________________

[[zip(itertools.repeat(x), dice_1) for x in dice_2]+[zip(itertools.repeat(x), dice_1) for x in dice_3]+[zip(itertools.repeat(x), dice_2) for x in dice_1]+[zip(itertools.repeat(x), dice_2) for x in dice_3]+[zip(itertools.repeat(x), dice_3) for x in dice_1]+[zip(itertools.repeat(x), dice_3) for x in dice_2]]

a_set = ((1, 4, 4, 4, 4, 4), (2, 2, 2, 5, 5, 5), (3, 3, 3, 3, 3, 6))

non_transitive = ((1, 1, 1, 1, 4, 6), (1, 1, 1, 2, 2, 7), (1, 2, 2, 3, 3, 3))

game_0 = [zip(itertools.repeat(x),this_list[0][1]) for x in this_list[0][0]]
game_1 = [zip(itertools.repeat(x),this_list[1][1]) for x in this_list[1][0]]
game_3 = [zip(itertools.repeat(x),this_list[2][1]) for x in this_list[2][0]]
game_4 = [zip(itertools.repeat(x),this_list[3][1]) for x in this_list[3][0]]
game_5 = [zip(itertools.repeat(x),this_list[4][1]) for x in this_list[4][0]]
game_6 = [zip(itertools.repeat(x),this_list[5][1]) for x in this_list[5][0]]

[game_count.append(1) for i in game_0[0] if max(i)>i[0]]


actual_dice = list(itertools.combinations_with_replacement(range(1,30), 6))

dice = list(itertools.combinations_with_replacement(range(1,8), 6))
"""There are 924 different dice 7Cr6 '(7 + 6 - 1)! / (6!(7 - 1)!)''"""
len(dice) = 924

combinations = list(itertools.combinations(dice, 3))
len(combinations) = 131054924

"""There are 3 games for each combination of 3 dice"""
number_of_games = 393164772

number_of_outcomes = 16512920424

"""For each game we need to get the number of games that P2 will win given every possible game"""
"""So, for each game there are 42 possible combinations of dice"""
def set_checker():
    dice = list(itertools.combinations_with_replacement(range(1,8), 6))
    combinations = list(itertools.combinations(dice, 3))
    generator = [itertools.combinations(n, 3) for n in itertools.combinations_with_replacement(range(1,8), 6)]




    nontransitive_sets = []

    for a_set in combinations:
        fifty = 0
        nontransitive_game = 0
        game_1 = []
        game_2 = []
        game_3 = []
        for x in itertools.permutations(a_set[0],len(a_set[1])):
            game_1.append(zip(x,a_set[1]))
        player_2_wins = 0
        for i in game_1:
            for x in i:
                if x[1] > x[0]:
                    player_2_wins += 1
            if player_2_wins > len(game_1)*6/2:
                nontransitive_game += 1

        for x in itertools.permutations(a_set[1],6):
            game_2.append(zip(x,a_set[2]))
        player_2_wins = 0
        for i in game_2:
            for x in i:
                if x[1] > x[0]:
                    player_2_wins += 1
            if player_2_wins > len(game_2)*6/2:
                nontransitive_game += 1

        for x in itertools.permutations(a_set[2],6):
            game_3.append(zip(x,a_set[3]))
        player_2_wins = 0
        for i in game_3:
            for x in i:
                if x[1] > x[0]:
                    player_2_wins += 1
            if player_2_wins > len(game_3)*6/2:
                nontransitive_game += 1

        if nontransitive_game = 3:
            nontransitive_sets.append(a_set)
    return(len(nontransitive_sets))
