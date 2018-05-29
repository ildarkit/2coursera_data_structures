# python3
import sys


class Node:
    def __init__(self):
        self.childs = {'left': None, 'right': None}
        self._child_index = None

    def __str__(self):
        return self._child_index

    def set_child_index(self, inx):
        self._child_index = inx

    @property
    def child_index(self):
        return self._child_index

    @property
    def left(self):
        return self.childs['left']

    @property
    def right(self):
        return self.childs['right']

    def add_child(self, node):
        if self.childs['left'] is None:
            self.childs['left'] = node
        else:
            self.childs['right'] = node


def get_tree(nodes):
    root = None
    n = len(nodes)
    tree = [Node() for _ in range(n)]
    for child_index in range(n):
        parent_index = nodes[child_index]
        if parent_index == -1:
            root = child_index
        else:
            tree[parent_index].set_child_index(child_index)
            tree[parent_index].add_child(tree[child_index])
    return tree, root


def get_leaf(tree, root):
    if not tree:
        return
    queue = list()
    queue.append(tree)
    node = None
    while queue:
        node = queue.pop()
        if node.left is not None:
            queue.insert(0, node.left)
        if node.right is not None:
            queue.insert(0, node.right)
    return node


# TODO search path to the root
def reverse(leaf):
    pass


if __name__ == '__main__':
    _ = sys.stdin.readline()
    nodes = list(map(int, sys.stdin.readline().split()))
    print(get_leaf(*get_tree(nodes)))

