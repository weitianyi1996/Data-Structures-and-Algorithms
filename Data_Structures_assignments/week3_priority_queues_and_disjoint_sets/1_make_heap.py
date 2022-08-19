# python3

# in-place solution
class Heap:
    # transform array to binary min heap
    def __init__(self, input_array):
        self.input_array = input_array
        self.swap_array = []
    #
    # def parent(self, i):
    #     return i//2

    def left_child(self, i):
        return 2*i+1  # as python is 0-based index

    def right_child(self, i):
        return 2*i+2

    def sift_down(self, i):
        min_index = i
        size = len(self.input_array)
        l = self.left_child(i)
        if l < size and self.input_array[l] < self.input_array[min_index]:
            min_index = l
        r = self.right_child(i)
        if r < size and self.input_array[r] < self.input_array[min_index]:
            min_index = r
        # swap array[i] with array[min_index]
        if i != min_index:
            val = self.input_array[i]
            self.input_array[i] = self.input_array[min_index]
            self.input_array[min_index] = val

            self.swap_array.append((i, min_index))   # store this two index
            self.sift_down(min_index)

    def construct_heap(self):
        for i in range(len(self.input_array)//2, -1, -1):
            self.sift_down(i)

    # def return_swaps(self):
    #     res = []
    #     res.append(int(len(self.swap_array)/2))  # num of swap times
    #     for ele in self.swap_array:
    #         res.append(ele)
    #     return res

# heap1 = Heap([5,4,3,2,1])
# heap1.construct_heap()
# print(heap1.return_swaps())


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    heap1 = Heap(data)
    heap1.construct_heap()
    swaps = heap1.swap_array

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()