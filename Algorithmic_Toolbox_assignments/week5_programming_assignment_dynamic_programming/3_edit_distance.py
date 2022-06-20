# Uses python3
import numpy as np

# dp[11,0] --> (0,11) in zuobiao
def edit_distance(s, t):
    # s- "edit"(horizontal)
    # t: "distancekk"( vertical)
    len_s, len_t = len(s), len(t)
    dp_matrix = np.zeros(shape=(len_t+1, len_s+1))  # 11*5

    for i in range(len_t+1):
        dp_matrix[i, 0] = i
    for j in range(len_s+1):
        dp_matrix[0, j] = j
    for row in range(1, len_s+1):# row, col is opposite in np matrix
        for col in range(1, len_t+1):
            # print(col, row)
            if t[col-1] == s[row-1]:
                dp_matrix[col, row] = min(
                    dp_matrix[col, row-1] + 1,
                    dp_matrix[col-1, row] + 1,
                    dp_matrix[col-1, row-1],
                )
            else:
                dp_matrix[col, row] = min(
                    dp_matrix[col, row-1] + 1,
                    dp_matrix[col-1, row] + 1,
                    dp_matrix[col-1, row-1] + 1,  # need to to replace the last character
                )
            # print(dp_matrix)
    return dp_matrix[-1, -1]



# print(edit_distance("editing","distance"))

if __name__ == "__main__":
    print(edit_distance(input(), input()))
