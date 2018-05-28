# python3

import sys


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        elif self.bracket_type == '{' and c == '}':
            return True
        elif self.bracket_type == '(' and c == ')':
            return True
        return False


def check_brackets(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.insert(0, Bracket(next, i + 1))

        elif next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return i + 1
            top = opening_brackets_stack.pop(0)
            if not top.match(next):
                return i + 1
    return 'Success' if not opening_brackets_stack else opening_brackets_stack[0].position


if __name__ == "__main__":
    text = sys.stdin.read()
    print(check_brackets(text))
