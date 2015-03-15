"""
Made by: Benjamin Maxwell (brm1921@g.rit.edu)
"""
import math

def decToBi(negateMethod, number):
    if number == 0:
        return "0"
    bit = number % 2
    if bit == 0 and number // 2 == 0:
        return ""
    return decToBi(negateMethod, number // 2) + str(bit)

def biToDec(number):
    if number == "":
        return 0
    return ((math.pow(2, len(number) -1 ) * int(number[0])) + biToDec(number[1:]))

def main():

    while True:
        print("What number do you want to convert to? ( Enter '...' to quit")
        print("Binary to Decimal? (b)")
        print("Decimal to Binary? (d)")
        mode = input(": ")
        if mode.lower() == "d":
            number = int(input("Enter a decimal number: "))
            negateMethod = "2"
            if int(number) < 0:
                negateMethod = input("One's comlement (1) or Two's comlement (2)?: ")
            print(decToBi(negateMethod, abs(number)))
        elif mode.lower() == "b":
            number =  input("Enter a binary number: ")
            print(int(biToDec(number)))
        elif mode == "...":
            break
        else:
            print("Unrecognized symbol")

main()