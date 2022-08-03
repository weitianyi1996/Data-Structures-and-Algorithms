# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


# # Replace this code with a faster implementation
# # this is from child node to parent node, try to start from different leaf nodes
# maxHeight = 0
# for vertex in range(self.n):
#         height = 0
#         i = vertex
#         while i != -1:
#                 height += 1
#                 i = self.parent[i]
#         maxHeight = max(maxHeight, height);
# return maxHeight;



# input - [4,-1,4,1,1]
# - 0 index, 0,1,2,3,4 - these are the nodes. so node 0's parent node is 4, node 1's parent node is itself
# Tree
# children = [[],[3,4],[],[],[0,2] ]
# parent = [4,-1,4,1,1]
# root = 1 (node 1)


class TreeHeight:
    def read(self):  # construct this tree structure based on input
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))  # parent node index
        self.children = [[] for _ in range(self.n)]
        self.root = None
        for index, value in enumerate(self.parent):
            if value == -1:  # this is root node
                self.root = index
            else:
                self.children[value].append(index)  # add to parent node- children list

    def compute_height(self, root):
        max_height = 0
        for i in range(len(self.children[root])):
            max_height = max(max_height, self.compute_height(self.children[root][i]))
        return max_height+1

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height(tree.root))


threading.Thread(target=main).start()