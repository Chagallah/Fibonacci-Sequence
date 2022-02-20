

def CheckIfFibonacci():
    numberToCheck = int(input("Enter number here: "))
    numZero = 0
    numOne = 1
    numTwo = 1

    if(numberToCheck == 0 or numberToCheck == 1):
        print("The number is a part of Fibonacci")

    else:
        while numZero < numberToCheck:
            numZero = numOne + numTwo
            numTwo = numOne
            numOne = numZero

    if numZero == numberToCheck:
        print("The number is part of Fibonacci")
    else:
        print("Number is not part of Fibonacci")
CheckIfFibonacci()