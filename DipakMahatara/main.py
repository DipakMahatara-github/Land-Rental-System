
from operations import *
def main():
    while True:
        print("Choose one valid option: ")
        print("1. Check availability")
        print("2. Rent land")
        print("3. Return Land")
        print("q. Exit")
        userInput=input("your choice?  ")
        if userInput=="1":
            checkAvailablility()
        elif userInput=="2":
            rentLand(input("Enter the kita no. of the land you want to rent: "))
        elif userInput=="3":
            returnLand(input("Enter the kita no. of the land you want to return: "))
        elif userInput=="q":
            break
        else:
            print("Invalid option.")
    print("Thanks for choosing us!")
#Calling part
print("TechnoPropertyNepal Pvt. ltd.")
main()