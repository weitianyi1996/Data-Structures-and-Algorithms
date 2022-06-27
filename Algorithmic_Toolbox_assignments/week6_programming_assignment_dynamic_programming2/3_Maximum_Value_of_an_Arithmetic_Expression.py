# Uses python3
import numpy as np


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(digits, ops):
    #write your code here
    # input dataset: 1+2-3*4-5
    n = len(digits)
    min_dp_matrix = np.zeros(shape=(n, n))
    max_dp_matrix = np.zeros(shape=(n, n))

    # fill the main digonal line
    for i in range(n):
        min_dp_matrix[i, i] = digits[i]
        max_dp_matrix[i, i] = digits[i]
    for s in range(1, n-1):
        for i in range(0, n-s):
            j = i+s  #
            # need to get [i,j]
            min_dp_matrix[i,j], max_dp_matrix[i,j] = min_and_max(i,j, min_dp_matrix, max_dp_matrix, ops)
    print(max_dp_matrix)
    return max_dp_matrix[0, -1]


def min_and_max(i, j, min_dp_matrix, max_dp_matrix, ops):
    # return the min, max between
    min_v = float("inf")
    max_v = float("-inf")
    for mid in range(i+1, j):  # [i,mid], [mid+1,j]
        l_min, l_max = min_dp_matrix[i, mid], max_dp_matrix[i, mid]
        r_min, r_max = min_dp_matrix[mid+1, j], max_dp_matrix[mid+1, j]
        print(l_min, l_max)
          # ops[mid] - this is the operation to perform
        min_v = min(evalt(l_min, r_min, ops[mid]), min_v)
        min_v = min(evalt(l_min, r_max, ops[mid]), min_v)
        min_v = min(evalt(l_max, r_min, ops[mid]), min_v)
        min_v = min(evalt(l_max, r_max, ops[mid]), min_v)

        max_v = max(evalt(l_min, r_min, ops[mid]), max_v)
        max_v = max(evalt(l_min, r_max, ops[mid]), max_v)
        max_v = max(evalt(l_max, r_min, ops[mid]), max_v)
        max_v = max(evalt(l_max, r_max, ops[mid]), max_v)
    return min_v, max_v




print(get_maximum_value(digits=[1,2,3,4,5], ops=["+","-","*","-"]))

# if __name__ == "__main__":
# ops_list = ["+", "-", "*"]

#     print(get_maximum_value(input()))