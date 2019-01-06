number = int(input("Enter number: "))
listOfNumeral = []

while (number!=0):
    curNumeral = number % 10
    listOfNumeral.append(curNumeral)
    number //= 10

listOfNumeral.reverse()

for i in range(0, 5):
    print("{} number is {}".format(i+1, listOfNumeral[i]))
