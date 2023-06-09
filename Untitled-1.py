def one_to_nine_polish(digit):
  if digit == 1:
    return 'jeden'
  elif digit == 2:
    return 'dwa'
  elif digit == 3:
    return 'trzy'
  elif digit == 4:
    return 'cztery'
  elif digit == 5:
    return 'pięć'
  elif digit == 6:
    return 'sześć'
  elif digit == 7:
    return 'siedem'
  elif digit == 8:
    return 'osiem'
  elif digit == 9:
    return 'dziewięć'


def teen_to_polish(digit):
  if digit == 11:
    return 'jedenaście'
  elif digit == 12:
    return 'dwanaście'
  elif digit == 13:
    return 'trzynaście'
  elif digit == 14:
    return 'czternaście'
  elif digit == 15:
    return 'piętnaście'
  elif digit == 16:
    return 'szesnaście'
  elif digit == 17:
    return 'siedemnaście'
  elif digit == 18:
    return 'osiemnaście'
  elif digit == 19:
    return 'dziewiętnaście'


def tens_to_polish(digit):
  if digit == 1:
    return 'dziesięć'
  elif digit == 2:
    return 'dwadzieścia'
  elif digit == 3:
    return 'trzydzieści'
  elif digit == 4:
    return 'czterdzieści'
  elif digit == 5:
    return 'pięćdziesiąt'
  elif digit == 6:
    return 'sześćdziesiąt'
  elif digit == 7:
    return 'siedemdziesiąt'
  elif digit == 8:
    return 'osiemdziesiąt'
  elif digit == 9:
    return 'dziewięćdziesiąt'


def hundred_to_polish(digit):
  if digit == 1:
    return 'sto'
  elif digit == 2:
    return 'dwieście'
  elif digit == 3:
    return 'trzysta'
  elif digit == 4:
    return 'czterysta'
  elif digit == 5:
    return 'pięćset'
  elif digit == 6:
    return 'sześćset'
  elif digit == 7:
    return 'siedemset'
  elif digit == 8:
    return 'osiemset'
  elif digit == 9:
    return 'dziewięćset'


def thousand_to_polish(digit): 
  if digit == 1:
    return 'tysiąc'
  elif 1 < digit <= 4:
    return one_to_nine_polish(digit) + ' tysiące'
  elif 4 < digit <= 9:
    return one_to_nine_polish(digit) + ' tysięcy'


def number_to_polish(number):
  thousands = number // 1000
  hundreds = number % 1000 // 100
  tens = number % 100 // 10
  unity = number % 10
  
  thousands_text = thousand_to_polish(thousands)
  hundreds_text = hundred_to_polish(hundreds)
  
  if tens > 1 or unity == 0:
    tens_text = tens_to_polish(tens)
  else:
    tens_text = None
    
  if tens == 1 and unity > 0:
    ones_text = teen_to_polish(tens*10 + unity)
  else:
    ones_text = one_to_nine_polish(unity)

  result = ""
  if thousands_text is not None:
    result += thousands_text
  if hundreds_text is not None:
    result += hundreds_text
  if tens_text is not None:
    result += tens_text
  if ones_text is not None:
    result += ones_text
  return result


length = 0
for number in range(1, 1001):
  text_number = number_to_polish(number)
  print(f'Liczba: {text_number}, dlugosc: {len(text_number)}')
  length += len(text_number)
  print(f'Calkowita dlugosc: {length}\n')
print(f'Ostateczny wynik: {length}')       