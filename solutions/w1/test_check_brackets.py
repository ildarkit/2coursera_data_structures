import unittest
from pathlib import Path

from check_brackets import check_brackets

TESTS = '../../w1/check_brackets_in_code/tests/'


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
                        test_or_result_data = test_or_result_data.rstrip()
                        files[key].append(test_or_result_data)
                        method(self, files[key])
                else:
                    files[file_name.name] = [test_or_result_data]
    return wrapper


class CheckBracketsCases(unittest.TestCase):

    @get_tests
    def test_brackets(self, args):
        self.assertEqual(check_brackets(args[0]), args[1])
