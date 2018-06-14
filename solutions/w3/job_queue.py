# python3


class JobQueue:

    def __init__(self):
        self.num_workers = None
        self.next_free_time = None
        self.jobs = None
        self.next_worker = -1

    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.next_free_time = [(0, -1)] * self.num_workers  # next time and number of worker
        self.jobs = list(map(int, input().split()))
        len_jobs = len(self.jobs)
        self.assigned_workers = [None] * len_jobs
        self.start_times = [None] * len_jobs
        assert m == len(self.jobs)

    def set_data(self, jobs, workers):
        """
        Data for tests.
        :param jobs:
        :param workers:
        :return: None
        """
        self.num_workers = workers
        self.next_worker = -1
        self.next_free_time = [(0, -1)] * self.num_workers
        self.jobs = jobs
        len_jobs = len(self.jobs)
        self.assigned_workers = [None] * len_jobs
        self.start_times = [None] * len_jobs

    def get_answer(self):
        """
        Response for tests.
        :return: str
        """
        result = list()
        for i in range(len(self.jobs)):
            result.append(' '.join(map(str, [self.assigned_workers[i], self.start_times[i]])))
        return '\n'.join(result)

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i])

    # def assign_jobs_naive(self):
    #     # starter slow implementation
    #     self.assigned_workers = [None] * len(self.jobs)
    #     self.start_times = [None] * len(self.jobs)
    #     for i in range(len(self.jobs)):
    #         next_worker = 0
    #         for j in range(1, self.num_workers):
    #             if self.next_free_time[j] < self.next_free_time[next_worker]:
    #                 next_worker = j
    #         self.assigned_workers[i] = next_worker
    #         self.start_times[i] = self.next_free_time[next_worker]
    #         self.next_free_time[next_worker] += self.jobs[i]

    def assign_jobs(self):
        """
        Faster implementation with priority queue (min-heap binary tree).
        """
        len_jobs = len(self.jobs)

        for i in range(len_jobs):

            next_time = self.extract_min()

            _next_worker = next_time[1]
            if _next_worker == -1:
                self.next_worker += 1
                _next_worker = self.next_worker
            self.assigned_workers[i] = _next_worker
            self.start_times[i] = next_time[0]
            _next_time = next_time[0] + self.jobs[i]
            self.insert((_next_time, _next_worker))

    def extract_min(self):
        """
        Get min element from root of heap.
        :return: tuple of next time and worker
        """
        result = self.next_free_time[0]
        self.next_free_time[0] = self.next_free_time[-1]
        self.next_free_time.pop()
        self.sift_down(0)
        return result

    def sift_down(self, i):
        size = len(self.next_free_time)
        min_index = i
        l = self.left_child(i)
        # jobs with a shorter execution time have a higher priority
        # if the execution time is the same, then the priority has a worker with a smaller index
        if l <= size - 1 and (self.next_free_time[l][0] < self.next_free_time[min_index][0] or (
                self.next_free_time[l][0] == self.next_free_time[min_index][0] and
                self.next_free_time[l][1] < self.next_free_time[min_index][1])):
            min_index = l
        r = self.right_child(i)
        if r <= size - 1 and (self.next_free_time[r][0] < self.next_free_time[min_index][0] or (
                self.next_free_time[r][0] == self.next_free_time[min_index][0] and
                self.next_free_time[r][1] < self.next_free_time[min_index][1])):
            min_index = r
        if i != min_index:
            self.next_free_time[i], self.next_free_time[min_index] = (self.next_free_time[min_index],
                                                                      self.next_free_time[i])
            self.sift_down(min_index)

    def left_child(self, i):
        return i*2 + 1

    def right_child(self, i):
        return i*2 + 2

    def parent(self, i):
        return (i - 1) // 2

    def insert(self, p):
        self.next_free_time.append(p)
        self.sift_up(len(self.next_free_time) - 1)

    def sift_up(self, i):
        while i > 0 and (self.next_free_time[self.parent(i)][0] > self.next_free_time[i][0] or (
                self.next_free_time[self.parent(i)][0] == self.next_free_time[i][0] and
                self.next_free_time[self.parent(i)][1] > self.next_free_time[i][1])):
            _parent = self.parent(i)
            self.next_free_time[_parent], self.next_free_time[i] = self.next_free_time[i], self.next_free_time[_parent]
            i = _parent

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()


if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

