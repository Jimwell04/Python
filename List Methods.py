# List Methods

numbers = [1,2,3,4,5,6,7,8,9]

print(numbers)

print(8 in numbers)

i = 0
while i <= 10:
    numbers.append(numbers[-1] + 1)
    i = i + 1
    
numbers.insert(0, 0)

print(numbers)

numbers.remove(3)

print(3 in numbers)
print(numbers)

numbers.clear()

print(numbers)