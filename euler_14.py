"""The following iterative sequence is defined for the set of positive integers.

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
    """

def longest_collatz_sequence():
    """Identify the longest collatz sequence under 1000000."""
    length = list()
    for i in range(500000, 900000):
        if not is_even(i):
            length.append([i, len(get_collatz_sequence(i))])
    return length


def get_collatz_sequence(start):
    """Generate a sequence of numbers that follow the collatz rule.

        1. if n is even:
                return n/2
        2. if n is odd:
                return 3n + 1
    """
    sequence_item = start
    sequence = [start]

    while sequence_item != 1:
        if is_even(sequence_item):
            sequence_item = sequence_item / 2
        else:
            sequence_item = (sequence_item * 3) + 1

        sequence.append(sequence_item)
    return sequence


def is_even(integer):
    """Return a bool if a number is odd or even."""
    if integer % 2 == 0:
        return True
    else:
        return False
