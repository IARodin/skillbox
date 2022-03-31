
count_n = int(input('Кол-во чисел в списке: '))
list_num = []
count_i = []
summ_i = 0 
for num in range(1, count_n + 1):
    number = int(input(f'Ведите {num} число: '))
    list_num.append(number)

div_num = int(input('Введите делитель: '))

for div in list_num:
    if div % div_num == 0:
        count_i.append(div)
        print(f'Индекс числа {div}: {len(count_i)}')

for index in range(len(count_i)):
    summ_i = index + 1 + summ_i   

print(f'Сумма индексов: {summ_i}')
