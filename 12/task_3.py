print('Задача 3. Апгрейд калькулятора')

def calculator():
    numb = int(input('Введите число: '))
    print()
    action = input('Для выбора действия введите команду:\nsum - Выводит сумму его цифр.\nmax - Выводит максимальную цифру.\nmin - Выводит минимальную цифру.\n')
    if action == 'sum':
        summN(numb)
        calculator()    
    elif action == 'max':
        maxNumb(numb)
        calculator()    
    elif action == 'min':
        minNumb(numb)
        calculator()    
    else:
        print('Ошибка ввода, нужно ввести "sum", "max", "min"')
        calculator()

def summN(numb):
    summN = 0
    while numb > 0:
        summN += numb % 10
        numb //= 10
    print(f'Сумма чисел равна {summN}')
def maxNumb(numb):
    maxNumb = 0
    while numb > 0:
        if numb % 10 >maxNumb:
            maxNumb = numb % 10
        numb //= 10    
    numb //= 10    
    print(f'Максимальное число: {maxNumb}')   
def minNumb(numb):
    minNumb = numb % 10
    while numb > 0:
        if minNumb >= numb % 10:
            minNumb = numb % 10
        numb //= 10    
    print(f'Минимальное число: {minNumb}')   
calculator()        


# Степан, как и большая часть населения планеты,
# для расчёта суммы и разности чисел использует калькулятор.
# 
# Однако в работе ему нужно
# делать не только  обычные действия вроде сложения и вычитания,
# а делать что-то вручную он уже устал.
# 
# Поэтому Степан решил немного расширить функциональность своего калькулятора.
# 
# Напишите программу,
# которая спрашивает у пользователя число и действие, 
# которое нужно с ним сделать: 
# вывести сумму его цифр,
# вывести максимальную цифру или вывести минимальную цифру. 
# 
# Каждое действие оформите в виде отдельной функции, 
# а основную программу зациклите.