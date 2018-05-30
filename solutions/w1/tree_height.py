# python3
import sys


class Node:
    def __init__(self):
        self.children = []
        self._child_index = None

    def __str__(self):
        return self._child_index

    def set_child_index(self, inx):
        self._child_index = inx

    @property
    def child_index(self):
        return self._child_index

    def get_children(self):
        return self.children

    def add_child(self, node):
        self.children.append(node)


def get_tree(nodes):
    n = len(nodes)
    tree = [Node() for _ in range(n)]
    for child_index in range(n):
        parent_index = nodes[child_index]
        if parent_index > -1:
            tree[child_index].set_child_index(child_index)
            tree[parent_index].add_child(tree[child_index])
    return tree


def level_traversal(queue):
    if not queue:
        return
    while queue:
        node = queue.pop(0)
        queue.extend(node.get_children())
    return node.child_index


# search path to the root
def tree_height(parents):
    tree = get_tree(parents)
    start_index = level_traversal(tree)
    parent_index = parents[start_index]
    i = 1
    while parent_index > -1:
        i += 1
        parent_index = parents[parent_index]
    return i


if __name__ == '__main__':
    _ = sys.stdin.readline()
    nodes = list(map(int, sys.stdin.readline().split()))
    print(tree_height(nodes))

