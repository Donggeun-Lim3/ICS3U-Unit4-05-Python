#!/usr/bin/env python3

# Created by Donggeun Lim
# Created on December 2020
# This is for loop program

def main():
    added_number = 0
    loop_counter = 0
    positive_string = input("Enter how many numbers you"
                            "wouldlike to add together : ")
    print("")
    try:
        positive_number = int(positive_string)

        if positive_number > 0:

            for loop_counter in range(positive_number):

                add_string = input("Enter integer to add : ")
                print("")

                try:
                    add_number = int(add_string)

                    if add_number > 0:
                        added_number = add_number + added_number
                    else:
                        continue

                except Exception:
                    print("This was not an integer")
                    break
            print("The total is : {}".format(added_number))
        elif positive_number == 0:
            print("This is 0")
        else:
            print("This is negative number")
    except Exception:
        print("This was not an integer")


if __name__ == "__main__":
    main()
