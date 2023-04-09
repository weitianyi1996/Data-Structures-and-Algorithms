#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
# threading.stack_size(2**25)  # new thread will get stack of such size
threading.stack_size(2**27)

class Tree:
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
        # self.key_list = [pos[0] for pos in tree]
        # self.left_list = [pos[1] for pos in tree]
        # self.right_list = [pos[2] for pos in tree]
        self.traverse_res = []

    def in_order_traverse(self, tree):
        if tree == -1:
            return

        self.in_order_traverse(self.left[tree])
        self.traverse_res.append(self.key[tree])
        self.in_order_traverse(self.right[tree])



def IsBinarySearchTree():
    # Implement correct algorithm here
    # input tree will look like this
    # tree = [[2, 1, 2], [1, -1, -1], [3, -1, -1]]

    # read from system inputs directly from here
    tree_ins = Tree()
    tree_ins.read()

    # edge case if tree is empty tree - input 0. No left_node_list, then return true
    if len(tree_ins.left) == 0:
        return True

    # traverse the tree and create the res list
    tree_ins.in_order_traverse(tree=0)

    # now i have the res list, go thru each that as a stack, to make sure later one is larger than previous
    for i in range(1, len(tree_ins.traverse_res)):
      if tree_ins.traverse_res[i] < tree_ins.traverse_res[i-1]:
          return False
    return True



def main():
  # nodes = int(sys.stdin.readline().strip())
  # tree = []
  # for i in range(nodes):
  #   tree.append(list(map(int, sys.stdin.readline().strip().split())))
  if IsBinarySearchTree():
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
