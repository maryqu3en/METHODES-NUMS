condition = True
while condition: 
    condition = False
    a = int(input(" Enter first value: "))
    b = int(input(" Enter second value: "))
    if a<=0 or b<=0:
        print("Enter positive none-null values")
        condition = True
    else:
        while b != 0:
            r = a % b 
            a = b
            b = r
print("GCD is ", a)
