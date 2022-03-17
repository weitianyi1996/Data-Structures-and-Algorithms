import sys


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    else:
        res = [0]*(1+n)
        res[1] = 1
        for i in range(2, n+1):
            res[i] = (res[i-2]+res[i-1])%10
        return res[-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
