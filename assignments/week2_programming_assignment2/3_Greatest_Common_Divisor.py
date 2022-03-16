# Uses python3
import sys


def gcd_naive(a, b):
    if min(a, b) == 0:
        return max(a, b)
    else:
        if a>=b:
            b_rm = a % b
            a = b
            return gcd_naive(a, b_rm)
        else: # a<b
            c = b
            b = a
            a = c
            return gcd_naive(a,b)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))