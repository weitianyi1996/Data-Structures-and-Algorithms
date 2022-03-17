# Uses python3
n = int(input())
numbers = [int(x) for x in input().split()]
numbers = sorted(numbers)
print(numbers[-1]*numbers[-2])


# # brute force
# def max_pairwise_product(numbers):
#     max_result = 0
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             max_result = max(numbers[i]*numbers[j], max_result)
#     return max_result

# scan twices
def max_pairwise_product(numbers):
    max_elm = sec_elm = 0
    for i in range(len(numbers)):
        max_elm = max(numbers[i], max_elm)
    max_index = numbers.index(max_elm)
    for j in range(len(numbers)):
        if numbers[j] > sec_elm and j != max_index:
            sec_elm = numbers[j]
    return max_elm*sec_elm

print(max_pairwise_product([1,2,3,5,5,2]))




