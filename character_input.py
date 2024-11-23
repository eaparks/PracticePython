"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to
them that tells them the year that they will turn 100 years old. Note: for this exercise,
the expectation is that you explicitly write out the year (and therefore be out of date the next year).
If you want to do this in a generic way, see exercise 39.
"""
import datetime

def get_input():
    name = input("Enter your name: ")
    age = int(input("Enter your age at the end of this year: "))
    return name, age

def main():
    # get input from user
    name, age = get_input()
    current_year = datetime.datetime.now().year

    # calculate 100 years from input year
    hundredth = current_year + (100 - age)

    # output 100th birthday year
    print(f'{name} will turn 100 years old in the year {hundredth}')


if __name__ == "__main__":
    main()
