import unittest
from pathlib import Path

from build_heap import HeapBuilder

TESTS = '../../w3/make_heap/tests/'


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
                        test_or_result_data = test_or_result_data.rstrip()
                        files[key].append(test_or_result_data)
                        method(self, files[key], key)
                else:
                    test_or_result_data = tests.readlines()[1]
                    test_data = list(map(int, test_or_result_data.rstrip().split()))
                    files[file_name.name] = [test_data]
    return wrapper


class BuildHeapCases(unittest.TestCase):

    def setUp(self):
        self.heap_builder = HeapBuilder()

    @get_tests
    def test_build_heap(self, args, key):
        print('test file {}'.format(key))
        self.heap_builder.set_data(args[0])
        self.heap_builder.generate_swaps()
        self.assertEqual(self.heap_builder.get_swaps(), args[1])
