# For Loops

numbers = [1,2,3,4,5,6,7,7]
print(numbers)

for i in numbers:
    print(i)
    
print()

i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1
    
print() 

for i in numbers:
    if i > 4:
        print(i)
        break
    else:
        continue
