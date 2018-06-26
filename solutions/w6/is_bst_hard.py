#!/usr/bin/python3

import sys
import threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size


def is_bst(tree):
    # Implement correct algorithm here
    keys = []
    return in_order_recursive(tree, 0, keys) if tree else not tree


def in_order_recursive(tree, vertex, keys):
    """
    Traversing a tree from left to right and
    comparing neighboring keys in pairs.
    :param tree: list of vertices (list of key with left and right children)
    :param vertex: index in tree
    :param keys: list of keys
    :return: True if tree is bst, else False
    """
    if vertex == -1:
        return True
    result = in_order_recursive(tree, tree[vertex][1], keys)
    if not result or (keys and keys[-1] > tree[vertex][0]):
        return False
    keys.append(tree[vertex][0])
    result = in_order_recursive(tree, tree[vertex][2], keys)
    return result


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if is_bst(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


if __name__ == '__main__':
    threading.Thread(target=main).start()
