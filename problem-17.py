import sys

ones = {
    0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
    7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = {
    2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
    7: 'seventy', 8: 'eighty', 9: 'ninety'}


def _divide(dividend, divisor, magnitude):
    modulo = dividend % divisor
    modulo_words = _number_to_words(dividend % divisor)
    if modulo != 0:
        modulo_words = f"and {modulo_words}"
    return _join(
        _number_to_words(dividend // divisor),
        magnitude,
        modulo_words
    )


def _join(*args):
    return ' '.join(filter(bool, args))


def _number_to_words(i):
    if i < 20:
        return ones[i]
    if i < 100:
        return _join(tens[i // 10], ones[i % 10])
    if i < 1000:
        return _divide(i, 100, 'hundred')
    if i == 1000:
        return 'one thousand'


# Run example:
# python problem-17.py $342$
if __name__ == '__main__':
    argvs = sys.argv
    number_in_words = _number_to_words(int(argvs[1].replace('$', '')))
    print(number_in_words)
    print(len(number_in_words.replace(' ', '')))
