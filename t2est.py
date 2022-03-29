text = input('Введите тескст: ')
num = input('Какую цифру ищем? ')
letter = input('Какую букву ищем? ')    
countNumb = 0
countLetter = 0  
    
for i in text:
    if i == num:
        countNumb += 1
print('Количество цифр: ', countNumb)
    
for i in text:
    if letter == i:
     countLetter += 1 
print('Количество букв:', countLetter)