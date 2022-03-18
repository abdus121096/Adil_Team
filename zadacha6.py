#6
numbers = [1,0,-2,4,3,6,6,3,5,8,4,2]
number = 1
while number != len(numbers):
    if numbers[number] > numbers[number - 1]:
        print(numbers[number], end=' ')
    number += 1
