# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # append to stack
            opening_brackets_stack.append(next)
        if next in ")]}":
            if opening_brackets_stack == []: # if opening brackets is empty
                return i
            last = opening_brackets_stack.pop()
            if (last == '{' and next == '}') | (last == '(' and next == ')') | (last == '[' and next == ']'):
                print(last, next, opening_brackets_stack, i)
                opening_brackets_stack.pop()
            else:
                return i
    return 'Success'

'''
{{}}[

{ -> [ '{' ] 
{ -> [ '{', '{' ]
} -> [ '{' ]
} -> [ ]
[ -> 

'''


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
