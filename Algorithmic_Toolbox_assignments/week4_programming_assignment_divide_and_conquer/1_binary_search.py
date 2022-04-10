def binary_search(keys, query):
    # keys # [1, 5, 8, 12, 13]
    # query 8, the element need to find
    l, r = 0, len(keys)-1
    while l <= r:
        mid = l+(r-l)//2
        if keys[mid] == query:
            return mid
        elif keys[mid] < query:
            l = mid+1
        else:  # keys[mid] < query
            r = mid-1
    return -1


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')

