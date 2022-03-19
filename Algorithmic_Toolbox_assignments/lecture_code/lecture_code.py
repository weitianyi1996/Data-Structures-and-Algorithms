# Fractional Knapsack
w_list= [w1, w2, ...,wn]
v_list = [v1, v2, ...,vn]

def fractional_knapsack ():
    res_dic = {}
    current_cap = 0
    sort_unit_value = sorted(w1 / v1, w2 / v2, …)
    while current_cap < W:
        item_n = 0
        sort_unit = sort_unit_value[item_n]  # current unit value for the item
        current_load_for_this_item = 0
        while current_cap < W and current_load_for_this_item < v_list[item_n]:
            current_cap += 1 * sort_unit
            current_load_for_this_item += 1 * sort_unit
        res_dic[item_n] = current_load_for_this_item
        item_n += 1  # next item
    return res_dic
