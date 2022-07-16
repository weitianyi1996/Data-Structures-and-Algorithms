# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]




def find_mismatch(text):
    opening_brackets_stack = []
    index_stack = []
    dic = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(next)
            index_stack.append(i+1)

        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0 or next != dic[opening_brackets_stack.pop()]:
                return i+1
            else:  # == pop
                index_stack.pop()
    return "Success" if len(opening_brackets_stack) == 0 else index_stack[0]

# print(find_mismatch("[](()"))




def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)



if __name__ == "__main__":
    main()