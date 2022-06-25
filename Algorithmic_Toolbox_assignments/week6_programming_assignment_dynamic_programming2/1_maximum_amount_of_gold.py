# Uses python3
import sys
import numpy as np


def optimal_weight(W, w):
    # write your code here
    # w - [1, 4, 8]
    dp_matrix = np.zeros(shape=(len(w)+1, W+1))
    for ind_row in range(1, len(w)+1):
        for ind_col in range(1, W+1):
            if ind_col >= w[ind_row-1]:  # have the capacity to load
                dp_matrix[ind_row, ind_col] = max(dp_matrix[ind_row-1, ind_col],  # not load the ith element, previous max weight before seeing this item
                                                  dp_matrix[ind_row-1, ind_col-w[ind_row-1]]+w[ind_row-1]  # load the ith element
                                                  )
            else:  # can not load this item
                dp_matrix[ind_row, ind_col] = dp_matrix[ind_row-1, ind_col]
    # print(dp_matrix)
    return int(dp_matrix[-1,-1])


# print(optimal_weight(10, [1, 4, 8]))

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
