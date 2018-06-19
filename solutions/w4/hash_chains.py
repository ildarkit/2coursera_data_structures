# python3
import sys


class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # array of chains
        self.elems = [[] for _ in range(self.bucket_count)]

    def set_tests_data(self, cases):
        """
        Cases for unit test
        :param cases: tests
        :return: None
        """
        self.cases = cases

    def _hash_func(self, s):
        """
        Polynomial hash function
        :param s: string for hashing
        :return: index of array (int)
        """
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def get_chain_key(self, key):
        return self.elems[self._hash_func(key)]

    def get_chain_index(self, ind):
        return reversed(self.elems[ind])

    def has_key(self, key):
        chain = self.get_chain_key(key)
        return key in chain

    def set_key(self, key):
        chain = self.get_chain_key(key)
        if key not in chain:
            chain.append(key)

    def del_key(self, key):
        chain = self.get_chain_key(key)
        if key in chain:
            chain.remove(key)

    def write_search_result(self, was_found, stream=sys.stdout):
        print('yes' if was_found else 'no', file=stream)

    def write_chain(self, chain, stream=sys.stdout):
        chain = ' '.join(chain)
        if chain:
            # added a space at the end of the line
            # for passing the tests from a test file
            chain += ' '
        print(chain, file=stream)

    def read_query(self):
        return Query(input().split())

    def process_query(self, query, stream=sys.stdout):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            self.write_chain(self.get_chain_index(query.ind), stream)
        elif query.type == 'find':
            self.write_search_result(self.has_key(query.s), stream)
        elif query.type == 'add':
            self.set_key(query.s)
        else:
            self.del_key(query.s)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

    def process_test_queries(self, stream=sys.stdout):
        """
        Method for running tests
        :param stream: used in print() to stream
        :return: None
        """
        for case in self.cases:
            self.process_query(Query(case), stream)


if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
