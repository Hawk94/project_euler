import itertools

def open_file():
    with open('p054_poker.txt', 'r') as f:
        reader = f.readlines()
    return reader

def parse_reader():
    games = open_file()
    hand_list = []
    hands = []

    for i in games:
        hand_list.append(i.split(" "))

    for i in hand_list:
        i[-1] = i[-1].strip('\n')

    return hand_list



def make_dictionary():
    my_list = parse_reader()
    game_dict = {}
    for a_game in range(len(my_list)):
        this_game = my_list[a_game]
        player_1 = this_game[:5]
        player_2 = this_game[5:]
        hand_1 = []
        hand_2 = []
        for card in player_1:
            hand_1.append([card[0],card[1]])
        for card in player_2:
            hand_2.append([card[0],card[1]])
        game_hands = [hand_1,hand_2]
        game_dict.update({a_game:game_hands})
    return game_dict

def make_number_rank():
    dictionary = make_dictionary()
    for key, value in dictionary.items():
        for i in value:
            for x in i:
                if x[0] == 'A':
                    x[0] = 14
                if x[0] == 'K':
                    x[0] = 13
                if x[0] == 'Q':
                    x[0] = 12
                if x[0] == 'J':
                    x[0] = 11
                if x[0] == 'T':
                    x[0] = 10
                else:
                    x[0] = int(x[0])
    return dictionary

def getDupes(l):
    seen = set()
    seen_add = seen.add
    for x in l:
        if x in seen or seen_add(x):
            yield x


def high_card(cards):
    high_card = max(cards)
    return high_card

def straight(cards):
    sorted_cards = sorted(cards)
    if sorted_cards[4] == sorted_cards[3]+1 == sorted_cards[2] + 2 == sorted_cards [1] + 3 == sorted_cards[0] + 4:
        return 'Straight'
    # ACE LOW STRAIGHT
    if sorted_cards[0] == 2:
        if sorted_cards[4] == 14:
            if sorted_cards[1] == sorted_cards[2] - 1 == sorted_cards[3] - 2:
                return 'Straight'

def flush(suits):
    if suits[0] == suits[1] == suits[2] == suits[3] == suits[4]:
        return 'Flush'

def pairs(cards):
    pair_count = 0
    for i in itertools.permutations(cards,2):
        if i[0] == i[1]:
            pair_count += 1
    if pair_count == 1:
        return('One Pair')
    if pair_count == 2:
        return('Two Pairs')
    # THREE of a KIND
    if pair_count == 6:
        return("Three of a Kind")
    # FULL HOUSE
    if pair_count == 8:
        return("Full House")
    if pair_count == 12:
        return("Four of a Kind")

def straight_flush(cards, suits):
    if flush(suits) == 'Flush':
        if straight(cards) == 'Straight':
            if max(cards) == 14:
                return 'Royal Flush'
            else:
                return 'Straight Flush'


def hand_analysis(cards, suits):
    hands_dict = {'High Card': 100, 'One Pair': 200, 'Two Pairs': 300, 'Three of a Kind': 400, 'Straight': 500, 'Flush:': 600, 'Full House': 700, 'Four of a Kind': 800, 'Straight Flush': 900, 'Royal Flush': 1000}
    result = []
    high_cards = []
    result_dict = {}
    try:
        high_cards.append(high_card(cards))
    except KeyError:
        high_cards.append(0)
    try:
        result.append(hands_dict[pairs(cards)])
    except KeyError:
        pass
    try:
        result.append(hands_dict[straight(cards)])
    except KeyError:
        pass
    try:
        result.append(hands_dict[flush(suits)])
    except KeyError:
        pass
    try:
        result.append(hands_dict[straight_flush(cards, suits)])
    except KeyError:
        pass
    try:
        max_result = max(result)
    except ValueError:
        max_result = 0

    result_dict.update({'the_high_cards':high_cards,'results':max_result})
    return result_dict



def make_hands(hand):
    cards_dict = {}
    player_1_cards = []
    player_2_cards = []
    player_1_suits = []
    player_2_suits = []
    for i in range(5):
        player_1_cards.append(hand[0][i][0])
        player_1_suits.append(hand[0][i][1])
        player_2_cards.append(hand[1][i][0])
        player_2_suits.append(hand[1][i][1])
    cards_dict.update({'cards_1': player_1_cards, 'cards_2': player_2_cards, 'suits_1': player_1_suits, 'suits_2': player_2_suits})
    return cards_dict

def game_player():
    my_dict = make_number_rank()
    winner_winner = []
    for number, game in my_dict.items():
        this_game = make_hands(game)
        player_1_results = hand_analysis(this_game['cards_1'], this_game['suits_1'])
        player_2_results = hand_analysis(this_game['cards_2'], this_game['suits_2'])
        try:
            player_1 = player_1_results['results']
        except TypeError:
            player_1 = player_1_results['the_high_cards']
        try:
            player_2 = player_2_results['results']
        except TypeError:
            player_2 = player_2_results['the_high_cards']

        print(max(player_1,player_1_results['the_high_cards'][0]),max(player_2,player_2_results['the_high_cards'][0]))
        if max(player_1,player_1_results['the_high_cards'][0]) > max(player_2,player_2_results['the_high_cards'][0]):
            winner_winner.append(player_1)

    return len(winner_winner)
