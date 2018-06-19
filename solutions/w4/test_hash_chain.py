import unittest
from pathlib import Path
from io import StringIO

from hash_chains import QueryProcessor

TESTS = '../../w4/hash_chains/tests/'


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
                    hash_cardinality = int(test_or_result_data[0])
                    test_queries = [case.rstrip().split() for case in test_or_result_data[2:]]
                    files[file_name.name] = [hash_cardinality, test_queries]
    return wrapper


class HashChainCases(unittest.TestCase):

    def setUp(self):
        self.resp = StringIO()

    def tearDown(self):
        self.resp.close()

    @get_tests
    def test_hash_chain(self, args, key):
        print('test file {}'.format(key))
        proc = QueryProcessor(args[0])
        proc.set_tests_data(args[1])
        proc.process_test_queries(self.resp)
        self.assertEqual(self.resp.getvalue(), args[2])
