import sys
import unittest
import threading
from pathlib import Path

from tree_orders import TreeOrders

TESTS = '../../w6/tree_orders/tests/'


def get_tests(method):
    def wrapper(self):
        files = {}
        absolute_path = Path(TESTS).absolute()
        for file_name in absolute_path.glob('*'):
            with file_name.open() as tests:
                if file_name.suffix == '.a':
                    test_or_result_data = tests.read()
                    key = file_name.name.split('.a')[0]
                    if key in files:
                        files[key].append(test_or_result_data)
                        method(self, files[key], key)
                else:
                    test_or_result_data = tests.readlines()
                    files[file_name.name] = [test_or_result_data]
    return wrapper


def readline(gen):
    def get_line():
        return next(gen)
    return get_line


def gen(lines):
    for line in lines:
        yield line


def tester(test, args):
    """
    Function is executed in a thread with a greater depth of recursion and a stack.
    """
    # replace stdin.readline with a generator
    sys.stdin.readline = readline(gen(args[0]))
    test.tree.read()
    test.assertEqual(" ".join(str(x) for x in test.tree.in_order()) + '\n' +
                     " ".join(str(x) for x in test.tree.pre_order()) + '\n' +
                     " ".join(str(x) for x in test.tree.post_order()) + '\n', args[1])


class TreeOrdersCases(unittest.TestCase):

    def setUp(self):
        self.tree = TreeOrders()


    @get_tests
    def test_tree_orders(self, args, key):
        print('test file {}'.format(key))
        t = threading.Thread(target=tester, args=[self, args])
        t.start()
        t.join()
