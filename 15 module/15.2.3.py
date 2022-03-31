list_dogs = [15,12,2,3,1]
list_dogs.sort()
list_dogs.reverse()
count = 0
for dog in list_dogs:
    count +=1
    print(f'{count}-ое место: {dog} очков')