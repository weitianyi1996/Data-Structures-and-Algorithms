# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    curr_dist = 0
    refill = 0
    while curr_dist < distance:
        max_dist = curr_dist + tank
        if max_dist >= distance:
            return refill
        elif (len(stops) > 0 and max_dist < stops[0]) or (len(stops) == 0 and max_dist < distance):    # cannot arrive
            return -1
        else:  # still not reach to end yet, neet to refill
            i = 0
            while i < len(stops) and stops[i] <= max_dist:
                i += 1
            curr_dist = stops[i-1]  # refill at this station
            refill += 1
            stops = stops[i:]


# print(compute_min_refills(700, 200, [100, 200, 300, 400]))

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))