def calculate_fibonacci(n):
    res = [0]*(1+n)
    if n <= 1:
        return n
    else:  # n > 2
        res[1] = 1
        for i in range(2, n+1):
            res[i] = res[i-2]+res[i-1]
        return res[-1]

n = int(input())
print(calculate_fibonacci(n))

