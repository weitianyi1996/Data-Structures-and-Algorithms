import sys
import random

#  hard!!!


def partition3(a, l, r):
    # return m1, m2 between which is a tier
    par_num = a[l]
    m1, m2 = l, r
    i = l+1
    while i <= m2:
        if a[i] < par_num:
            m1 += 1
            a[i], a[m1] = a[m1], a[i]
            i += 1
        elif a[i] > par_num:
            a[i], a[m2] = a[m2], a[i]
            m2 -= 1
        else:  # ==
            i += 1
    a[l], a[m1] = a[m1], a[l]
    return m1, m2

def partition2(a, l, r):
    # any index < j , that element <= A[l]
    # any index in (j, i], that element > A[l]
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    # m = partition2(a, l, r)
    # randomized_quick_sort(a, l, m - 1);
    # randomized_quick_sort(a, m + 1, r);
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1-1)
    randomized_quick_sort(a, m2+1, r)


# print(randomized_quick_sort([6,4,11,6,9,6,7,3], 0, 7))


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')