
n = input('Введите первое число: ')
k = input('Введите второе число: ')
c1 = 'Первое'
c2 = 'Второе'

def reverse(number, c):
  a = ''
  b = ''
  flag = False
  for symbol in number:
    if symbol != '.':
      a = symbol + a
    elif symbol == '.':
      break
  for symbol in number:
    if flag == True:
      b = symbol + b
    if symbol == '.':
      flag = True
  print(f'{c} число наоборот: {a}.{b} ')

# TODO оформить код по правилам PEP8
reverse(n, c1)
reverse(k, c2)
# TODO дополнить ответ выводом суммы полученных "наоборот" чисел:
# Введите первое число: 12.45
# Введите второе число: 34.54
# Первое число наоборот: 21.54
# Второе число наоборот: 43.45
