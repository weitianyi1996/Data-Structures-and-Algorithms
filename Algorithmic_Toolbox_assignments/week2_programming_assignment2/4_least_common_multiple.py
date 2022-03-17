# Uses python3
import sys


def lcm_naive(a, b):
    gcd_acc = 1
    common_gcd = gcd(a,b)
    while common_gcd > 1:
        gcd_acc = gcd_acc*common_gcd
        a = a / common_gcd
        b = b / common_gcd
        common_gcd = gcd(a, b)
    return int(gcd_acc*a*b)

def gcd(a,b):
    if b == 0:
        return a
    elif a >= b:
        b_rm = a % b
        a = b
        return gcd(a, b_rm)
    else:
        return gcd(b, a)

# print(lcm_naive(6,8))


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))
