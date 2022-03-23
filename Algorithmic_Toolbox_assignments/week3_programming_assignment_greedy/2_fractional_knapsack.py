# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    curr_cap = 0
    dic = {}
    for i, v in enumerate(weights):
        value_per_weight = values[i]/weights[i]
        dic[value_per_weight] = weights[i]  # max is wight
    sort_list = sorted(dic.keys(), reverse=True)
    p = 0

    while curr_cap < capacity and p < len(sort_list):
        load_cap_this_time = min(capacity-curr_cap, dic[sort_list[p]])
        value += sort_list[p]*load_cap_this_time
        curr_cap += load_cap_this_time
        p += 1  # move to next valuable item

    return float("{:0.4f}".format(value))


# print(get_optimal_value(1000, [30], [500]))

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]  # 60
    weights = data[3:(2 * n + 2):2]  # 20
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))