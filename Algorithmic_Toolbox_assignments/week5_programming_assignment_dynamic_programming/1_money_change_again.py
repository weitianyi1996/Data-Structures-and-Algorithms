# Uses python3
import sys

def get_change(m):
    # write your code here
    res_arr = [0 for _ in range(m+1)]  # include 0 index, $0, need return 0 bill
    res_arr[0], res_arr[1], res_arr[2], res_arr[3] = 0,1,2,1
    if m <= 3:
        return res_arr[m]
    else:
        for i in range(4, m+1):
            res_arr[i] = min(res_arr[i-1]+1, res_arr[i-3]+1, res_arr[i-4]+1)
        return res_arr[m]
# print(get_change(34))


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
