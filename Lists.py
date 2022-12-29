# Lists

names = ["Jimwell", "Jack", "Manuel", "Eric", "John"]


print(names)
print(names[0])
print(names[-1])
print(names[-2])

names[1] = "Jackie"
print(names)
print(names[0:3])

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])

print(squares[7:])  

print(squares[::2])
print(squares[2:8:3])

print(squares[1:-1])

nums = [5, 42, 7, 1, 0]
res = nums[::-1]
print(res) 

