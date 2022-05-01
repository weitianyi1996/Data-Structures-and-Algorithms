# merge sort

def merge_sort(input_list):
    #  one input list, return a final sorted array
    l = len(input_list)
    if l == 1:
        return input_list
    else:
        # solve below two subproblems
        sorted_list_1 = merge_sort(input_list[:(l//2)])
        sorted_list_2 = merge_sort(input_list[(l//2):])
        return merge_sorted_array(sorted_list_1, sorted_list_2)


def merge_sorted_array(list1, list2):
    # merge two sorted list into one sorted list"
    res_array = []
    while len(list1) > 0 and len(list2) > 0:
        list1_first = list1[0]
        list2_first = list2[0]
        if list1_first >= list2_first:
            res_array.append(list2_first)
            list2 = list2[1:]
        else:
            res_array.append(list1_first)
            list1 = list1[1:]
    if len(list1) > 0:
        res_array += list1
    if len(list2) > 0:
        res_array += list2
    return res_array


# print(merge_sorted_array([1,2,5], [3,6,7]))
print(merge_sort([7,2,5,3,7,13,1,6]))
