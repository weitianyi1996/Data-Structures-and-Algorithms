# python3
import sys


def compute_min_refills(distance, tank, stops):
    curr_dist = refill = 0
    stt_pointer = 0
    while curr_dist < distance:
        max_dist = curr_dist + tank
        if max_dist > distance:  # arrive
            return refill
        elif (stt_pointer < len(stops) and max_dist < stops[stt_pointer]) \
                or (stt_pointer >= len(stops) and max_dist < distance):  # next stop
            return -1  # cannot arrive next station or destination
        else:  # can arrive next stop
            while stt_pointer<len(stops) and stops[stt_pointer] < max_dist:  # reach as far as possible using current tank
                stt_pointer += 1
            curr_dist = stops[stt_pointer-1]  # refill at this station
            refill += 1



# print(compute_min_refills(950, 400, [200, 375, 550, 750]))
# print(compute_min_refills(700, 200, [100, 200, 300, 400]))

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
