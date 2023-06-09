cache_dict = {1: 1}


def count(number):
    if number not in cache_dict:
        if number % 2 == 0:
            cache_dict[number] = 1 + count(number / 2)
        else:
            cache_dict[number] = 1 + count(3 * number + 1)
    return cache_dict[number]


def collatz_search():
    biggest_collatz_sequence_count = 0
    collatz_sequence_count_number = 0
    for x in range(999999):
        collatz_sequence_count = count(x + 1)
        if collatz_sequence_count > biggest_collatz_sequence_count:
            biggest_collatz_sequence_count = collatz_sequence_count
            collatz_sequence_count_number = x + 1
    return biggest_collatz_sequence_count, collatz_sequence_count_number


# Run example:
# python problem-14.py
if __name__ == '__main__':
    biggest_csc, csc_number = collatz_search()
    print(f'biggest_collatz_sequence_count = {biggest_csc}')
    print(f'collatz_sequence_count_number = {csc_number}')
