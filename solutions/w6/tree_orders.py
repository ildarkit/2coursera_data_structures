# python3

import sys, threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:

    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for _ in range(self.n)]
        self.left = [0 for _ in range(self.n)]
        self.right = [0 for _ in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def in_order(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        return self.result

    def pre_order(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        return self.result

    def post_order(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that

        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.in_order()))
    print(" ".join(str(x) for x in tree.pre_order()))
    print(" ".join(str(x) for x in tree.post_order()))


if __name__ == '__main__':
    t = threading.Thread(target=main)
    t.start()
    t.join()
