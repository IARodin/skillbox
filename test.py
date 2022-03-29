def payment(starting_credit, years, percent):
  coefficient = percent * (1 + percent) ** years / ((1 + percent) ** years - 1)
  return round(coefficient * starting_credit, 2)


def percent_paid(credit, percent):
  return credit * percent


def credit_paid(starting_credit, credit, years, percent):
  return payment(starting_credit, years, percent) - percent_paid(credit, percent)


def debt(starting_credit, credit, years, percent):
  return credit - credit_paid(starting_credit, credit, years, percent)


def show_results(starting_credit, credit, years, percent, period):
  print('\nПериод:', period, end = '\n\n')
  print('Остаток долга на начало периода:',  credit)
  print('Выплачено процентов:', percent_paid(credit, percent))
  print('Выплачено тела кредита:', credit_paid(starting_credit, credit, years, percent))


credit = float(input('Введите сумму кредита: '))
years = int(input('На сколько лет выдан? '))
percent = float(input('Сколько процентов годовых? '))

starting_credit = credit

period = 1
while period < 4:
  show_results(starting_credit, credit, years, percent / 100, period)
  credit = debt(starting_credit, credit, years, percent / 100)
  period += 1

print('\nОстаток долга:', credit)
print('\n\n', '=' * 30, '\n\n')

years_prolongation = int(input('На сколько лет продляется договор? '))
percent_increase = float(input('Увеличение ставки до: '))

years = years - 3 + years_prolongation
starting_credit = credit

period = 1
while period <= years:
  show_results(starting_credit, credit, years, percent_increase / 100, period)
  credit = debt(starting_credit, credit, years, percent_increase / 100)
  period += 1

print('\nОстаток долга:', credit)