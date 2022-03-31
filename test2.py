number = int(input('Введите число: '))

def suma_number(number):
  suma = 0
  while number > 0:
    digit = number % 10
    suma = suma + digit
    number = number // 10
print('\nСумма цифр:', suma)

suma_number(number)

def count_number(number):
  countnumber = number
  digitcount = 0
  while countnumber > 0:
    digitcount += 1
    countnumber = countnumber // 10
print('Кол-во цифр в числе:', digitcount)

count_number(number)

def differ(suma, digitcount):
  diff = suma - digitcount
  print('Разность суммы и кол-ва цифр:', diff)

differ(suma, digitcount)