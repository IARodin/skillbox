
count_n = int(input('Кол-во чисел в списке: '))
list_num = []

for num in range(1, count_n + 1):
    number = int(input(f'Ведите {num} число: '))
    list_num.append(number)

div_num = int(input('Введите делитель: '))

for div in list_num:
    if div % div_num == 0:
        print(f'Индекс числа {div}: ') 