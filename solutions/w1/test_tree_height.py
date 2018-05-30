import unittest
from pathlib import Path

from tree_height import tree_height

TESTS = '../../w1/tree_height/tests/'


def get_tests(method):
    def wrapper(self):
        files = {}
        absolute_path = Path(TESTS).absolute()
        for file_name in absolute_path.glob('*'):
            with file_name.open() as tests:
                test_or_result_data = tests.read()
                if file_name.suffix == '.a':
                    key = file_name.name.split('.a')[0]
                    if key in files:
                        test_or_result_data = int(test_or_result_data.rstrip())
                        files[key].append(test_or_result_data)
                        method(self, files[key], key)
                else:
                    test_data = list(map(int, test_or_result_data.rstrip().split()))
                    test_data = test_data[1:]
                    files[file_name.name] = [test_data]
    return wrapper


class TreeHeightCases(unittest.TestCase):

    @get_tests
    def test_tree_height(self, args, key):
        print('test file {}'.format(key))
        self.assertEqual(tree_height(args[0]), args[1])
