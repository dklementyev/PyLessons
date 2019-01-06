for i in range(1, 100):
    valueForPrint = str()
    if(i % 3 == 0):
        valueForPrint = "Fizz"
    if(i % 5 ==0):
        valueForPrint += "Buzz"
    if(valueForPrint == ""):
        valueForPrint = str(i)
    print(valueForPrint)
