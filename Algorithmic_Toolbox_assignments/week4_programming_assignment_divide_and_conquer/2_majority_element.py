 # Uses python3
import sys
# http://users.ece.northwestern.edu/~dda902/336/hw4-sol.pdf


# wrapper function - to handle weird input format of the assignment requirement from coursera
def get_majority_element(a, left, right):
    # print(a, left, right) # [2, 3, 9, 2, 2] 0 5
    indicator = get_majority_element_value(a, left, right-1)
    if indicator is None:  # not have a major element
        return 0
    else:
        return 1

def get_majority_element_value(a, left, right):
    """
    :param a:
    :param left:
    :param right:
    :return: this func will return the major element of a list
    """
    if left == right:
        return a[left]
    # if left + 1 == right:
    #     return a[left]
    #write your code here
    mid = left+(right-left)//2
    # print(left, right)
    # print("this is mid {}".format(mid))
    l_major = get_majority_element_value(a, left, mid)  # make recursive call, include boundary
    r_major = get_majority_element_value(a, mid+1, right)
    if l_major == r_major:
        return l_major
    elif l_major is not None and get_frequency(l_major, a[left:(right+1)]) > (right-left+1)//2:
        return l_major
    elif r_major is not None and get_frequency(r_major, a[left:(right+1)]) > (right-left+1)//2:
        return r_major
    else:
        return None


def get_frequency(element, lst):
    cnt = 0
    for ele in lst:
        if ele == element:
            cnt += 1
    return cnt



# print(get_majority_element_value([512766168,717383758, 5, 126144732, 5, 573799007, 5, 5, 5, 405079772],0,9))
# print(get_majority_element([512766168,717383758, 5, 126144732, 5, 573799007, 5, 5, 5, 405079772],0,10))

# print(get_majority_element([2, 3, 9, 2, 2], 0, 4))
# print(get_majority_element([2, 3, 9, 2, 2], 0, 5))

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # if get_majority_element(a, 0, n) != -1:
    #     print(1)
    # else:
    #     print(0)
    print(get_majority_element(a, 0, n))