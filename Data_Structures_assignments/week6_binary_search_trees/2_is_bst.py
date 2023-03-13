#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


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

# wrong answer!!
# def IsBinarySearchTree(tree):
#   # Implement correct algorithm here
#   # input tree will look like this
#   # tree = [[2, 1, 2], [1, -1, -1], [3, -1, -1]]
#
#   key_list = [pos[0] for pos in tree]
#   left_list = [pos[1] for pos in tree]
#   right_list = [pos[2] for pos in tree]
#   for i in range(len(tree)):
#       left_i, right_i = left_list[i], right_list[i]
#       key_node = key_list[i]
#       key_left, key_right = key_list[left_i], key_list[right_i]
#       if left_i > -1 and key_node < key_left:
#           return False
#       if right_i > -1 and key_node > key_right:
#           return False
#
#   return True