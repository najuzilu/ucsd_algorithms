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
            opening_brackets_stack.append(Bracket(next, i))
        if next in ")]}":
            if len(opening_brackets_stack) == 0: # if opening brackets is empty
                return i + 1
            last = opening_brackets_stack.pop()[0]
            if (last == '{' and next != '}') | (last == '(' and next != ')') | (last == '[' and next != ']'):
                return i + 1
    if len(opening_brackets_stack) != 0:
        return opening_brackets_stack.pop()[1] + 1
    return 'Success'

def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
