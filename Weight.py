# Weight Calculator

loop = True

while (loop):

    weight = float(input("Weight: "))
    
    unit = input("(K)g or (L)bs: ")

    if unit.upper() == "K":
        loop = False
        converted = weight / 0.45
        print("Weight in Kg is: " + str(converted))
    elif unit.upper() == "L":
        loop = False
        converted = weight * 0.45
        print("Weight in Lbs is: " + str(converted))
    else:
        loop = True
        print("Invalid input type K or L")
    
    
