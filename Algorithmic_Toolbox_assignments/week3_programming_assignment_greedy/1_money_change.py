# Uses python3
import sys


# return min m, face value include 1,5,10
def get_change(m):
    num_change = 0
    while m > 0:
        if m >= 10:
            m -= 10
        elif 5 <= m < 10:
            m -= 5
        elif 1 <= m < 5:
            m -= 1
        num_change += 1
    return num_change


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
