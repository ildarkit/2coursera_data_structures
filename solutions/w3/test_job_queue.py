import unittest
from pathlib import Path

from job_queue import JobQueue

TESTS = '../../w3/job_queue/tests/'


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
                    test_or_result_data = tests.readlines()
                    test_data = list(map(int, test_or_result_data[1].rstrip().split()))
                    files[file_name.name] = [(test_data, int(test_or_result_data[0].split()[0]))]
    return wrapper


class JobQueueCases(unittest.TestCase):

    def setUp(self):
        self.job_queue = JobQueue()

    @get_tests
    def test_job_queue(self, args, key):
        print('test file {}'.format(key))
        self.job_queue.set_data(*args[0])
        self.job_queue.assign_jobs()
        self.assertEqual(self.job_queue.get_answer(), args[1])
