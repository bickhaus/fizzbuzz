#fizzbuzz

#for i in range(1,101):
#    if i % 3 == 0:
#        if i % 5 == 0:
#            print("FizzBuzz")
#        else:
#            print("Fizz")
#    elif i % 5 == 0:
#        print("Buzz")
#    else:
#        print(i)

for i in range(1,101):
    fbString = ""
    if i % 3 == 0:
        fbString += "Fizz"
    if i % 5 == 0:
        fbString += "Buzz"
    if len(fbString):
        print(fbString)
    else:
        print(i)
        
        
