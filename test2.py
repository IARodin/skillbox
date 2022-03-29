def calculator():
  numb = int(input('Введите число: '))
  action = int(input('Выберите действие:\n1 - вывести сумму цифр числа;\n2 - вывести наибольшую цифру цисла;\n3 - вывести наименьшую цифру числа: \n'))
  if action == 1:
    sum_numb(numb)
    calculator()
  elif action == 2:
    max_numb(numb)
    calculator()
  elif action == 3:
    min_numb(numb)
    calculator()
  else:
    print('\nОшибка ввода!')
    calculator()

def sum_numb(numb):
  sum_numb = 0
  while numb > 0:
    sum_numb += numb % 10
    numb //= 10
  print('Сумма цифр числа равна:', sum_numb, '\n')

def max_numb(numb):
  max_numb = 0
  while numb > 0:
    if numb % 10 > max_numb:
      max_numb = numb % 10
    numb //= 10
  print('Максимальная цифра в числе равна:', max_numb, '\n')

def min_numb(numb):
  min_numb = numb % 10
  while numb > 0:
    if min_numb >= numb % 10:
      min_numb = numb % 10
    numb //= 10 
  print('Минимальная цифра в числе равна:', min_numb, '\n')

calculator()