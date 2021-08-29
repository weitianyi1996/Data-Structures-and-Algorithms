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




