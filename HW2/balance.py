######################################################################################################
#Author: Paul Leone
#Date: 4/15/2020
#Program Filename: balance.py
#Description: Determine whether the paratheses are balanced or not
######################################################################################################

# balance.py
# ===================================================
# Using a stack to check for unbalanced parentheses
# ===================================================

import sys


# Checks whether the input string is balanced
# param: input string
# returns True if string is balanced, otherwise returns False

#parantheses to check
open_parans = ["[", "{", "("]
close_parans = ["]", "}", ")"]
def is_balanced(input_string):

    # initialize an empty list as the stack
    stack = []

    # iterate over each character in the string
    for i in input_string:
        """check the length of the input string"""
        if len(input_string) == 1:
            return False
        elif i in open_parans:
            """append to the stack"""
            stack.append(i)
        elif i in close_parans:
            """remove from the stack for unbalance"""
            j = close_parans.index(i)
            if ((len(stack) > 0) and (open_parans[j] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    # get input string
    _input_string = sys.argv[1]  # DO NOT MODIFY

    balanced = is_balanced(_input_string)

    if balanced:
        print("The string {} is balanced".format(_input_string))
    else:
        print("The string {} is not balanced".format(_input_string))