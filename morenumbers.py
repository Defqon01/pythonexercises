a = input("insert the first number: ")
b = input("insert the second number: ")
c = input("insert the third number: ")

if a >= b and a >= c:
    print (a)
elif b >= a and b >= c:
    print (b)
elif c >= a and c >= b:
    print (c)
else:
    print ("all numbers are equal")