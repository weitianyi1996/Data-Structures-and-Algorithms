# Uses python3
import sys

def optimal_sequence(n):
    if n ==1 :
        return 1
    elif n == 2:
        return [1,2]
    elif n == 3:
        return [1,3]
    elif n >= 4:
        num_opp_arr = [0, 0, 1, 1]  # op needed for [0, 1, 2, 3]
        # num_opp_arr[5], how many op needed to get 5
        # do a dp, planning array
        for plan_num in range(4, n):
            if plan_num%3 == 0 and plan_num%2 == 0:
                num_opp = min(num_opp_arr[plan_num//3], num_opp_arr[plan_num//2], num_opp_arr[plan_num-1])+1
            elif plan_num%3 != 0 and plan_num%2 == 0:
                num_opp = min(num_opp_arr[plan_num//2], num_opp_arr[plan_num-1])+1
            elif plan_num%3 == 0 and plan_num%2 != 0:
                num_opp = min(num_opp_arr[plan_num//3], num_opp_arr[plan_num-1])+1
            else:
                num_opp = num_opp_arr[plan_num-1]+1
            num_opp_arr.append(num_opp)
        # i want to see how we use dp array to get n so that we can simutlate the whole process to find and return the res array
        res_arr = []
        while n > 1:
            res_arr.append(n)
            if n%3 == 0 and n%2 == 0:
                if num_opp_arr[n//3] == min(num_opp_arr[n//3],num_opp_arr[n//2], num_opp_arr[n-1]):
                    n = n//3
                elif num_opp_arr[n//2] == min(num_opp_arr[n//3],num_opp_arr[n//2], num_opp_arr[n-1]):
                    n = n//2
                else:
                    n -= 1
            elif n%3 != 0 and n%2 == 0:
                if num_opp_arr[n//2] <= num_opp_arr[n-1]:
                    n = n//2
                else:
                    n -= 1
            elif n%3 == 0 and n%2 != 0:
                if num_opp_arr[n//3] <= num_opp_arr[n-1]:
                    n = n//3
                else:
                    n -= 1
            else:  # can not divide by 3 and by 2
                n -= 1
        res_arr.append(1)
        return reversed(res_arr)


# print(optimal_sequence(6))







input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
