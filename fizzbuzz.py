#fizzbuzz

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
        
        
