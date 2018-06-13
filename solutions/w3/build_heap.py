# python3


class HeapBuilder:

    def __init__(self):
        self._swaps = []
        self._data = []

    def read_data(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def set_data(self, data):
        self._data = data

    def get_swaps(self):
        result = list()
        result.append(str(len(self._swaps)))
        for swap in self._swaps:
            result.append(' '.join(map(str, swap)))
        return '\n'.join(result)

    def write_response(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def generate_swaps_naive(self):
        """
        The following naive implementation just sorts
        the given sequence using selection sort algorithm
        and saves the resulting sequence of swaps.
        This turns the given array into a heap,
        but in the worst case gives a quadratic number of swaps.
        """

        for i in range(len(self._data)):
            for j in range(i + 1, len(self._data)):
                if self._data[i] > self._data[j]:
                    self._swaps.append((i, j))
                    self._data[i], self._data[j] = self._data[j], self._data[i]

    # more efficient implementation with heap
    def generate_swaps(self):
        self.build_heap()

    def build_heap(self):
        size = len(self._data)
        for i in range((size // 2) - 1, -1, -1):
            self.sift_down(i)

    def sift_down(self, i):
        size = len(self._data)
        min_index = i
        l = self.left_child(i)
        if l <= size - 1 and self._data[l] < self._data[min_index]:
            min_index = l
        r = self.right_child(i)
        if r <= size - 1 and self._data[r] < self._data[min_index]:
            min_index = r
        if i != min_index:
            self._data[i], self._data[min_index] = self._data[min_index], self._data[i]
            self._swaps.append((i, min_index))
            self.sift_down(min_index)

    def left_child(self, i):
        return i*2 + 1

    def right_child(self, i):
        return i*2 + 2

    def solve(self):
        self.read_data()
        self.generate_swaps()
        self.write_response()


if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.solve()