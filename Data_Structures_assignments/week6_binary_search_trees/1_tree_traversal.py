# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

        # don't add these list in each function, otherwise when recursive, would rewrite all res to empty!
        self.in_order_res = []
        self.pre_order_res = []
        self.post_order_res = []

    # def get_left(self, index):
    #     return index*2+1
    # def get_right(self, index):
    #     return index*2+2

    def in_order_traversal(self, tree): # here tree refers to the root node index
        if tree == -1:  # here tree is index
            return
        self.in_order_traversal(self.left[tree])
        self.in_order_res.append(self.key[tree])
        self.in_order_traversal(self.right[tree])

        return self.in_order_res

    def pre_order_traversal(self, tree):  # here tree refers to the root node index
        if tree == -1:  # here tree is index
            return
        self.pre_order_res.append(self.key[tree])
        self.pre_order_traversal(self.left[tree])
        self.pre_order_traversal(self.right[tree])

        return self.pre_order_res

    def post_order_traversal(self, tree):  # here tree refers to the root node index
        if tree == -1:  # here tree is index
            return
        self.post_order_traversal(self.left[tree])
        self.post_order_traversal(self.right[tree])
        self.post_order_res.append(self.key[tree])

        return self.post_order_res


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.in_order_traversal(0)))
    print(" ".join(str(x) for x in tree.pre_order_traversal(0)))
    print(" ".join(str(x) for x in tree.post_order_traversal(0)))


threading.Thread(target=main).start()
