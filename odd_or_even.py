"""
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""


def main():
    # get user input
    input_num = int(float(input("Enter a number: ")))   # input might be eg, 3.7
    if input_num % 2 == 0:
        print(f"{input_num} is EVEN")
        if input_num % 4 == 0:
            print(f"{input_num} is evenly divided by 4")
    else:
        print(f"{input_num} is ODD")


if __name__ == '__main__':
    main()
