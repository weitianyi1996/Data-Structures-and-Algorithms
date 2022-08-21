# python3
# next_free_time = [3, 0]
# for i in range(2):
#     print(i)
# next_worker = min(range(2), key=lambda w: next_free_time[w])  # ! i need to compare range(2), based on lambda function!
# print(next_worker)

# thanks to this gives me inspiration: https://github.com/maxis42/Data-Structures-Algorithms-Coursera-UCSD-HSE/blob/master/2%20Data%20Structures/Homeworks/Week%203/2_job_queue/job_queue.py
# https://github.com/ivankliuk/coursera-data-structures-algorithms/blob/master/data-structures/priority-queues-and-disjoint-sets/job_queue.py

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


# def assign_jobs(n_workers, jobs):
#     # TODO: replace this code with a faster algorithm.
#     result = []
#     next_free_time = [0] * n_workers
#     for job in jobs:
#         next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
#         result.append(AssignedJob(next_worker, next_free_time[next_worker]))
#         next_free_time[next_worker] += job
#
#     return result
class Worker:
    def __init__(self, id):
        self.id = id
        self.worktime = 0


def sift_down_worker(worker_array, i):
    first_prior_index = i
    l_child = i*2+1
    r_child = i*2+2

    # need to sift down and replace with the left child
    # left child priority is higher - worktime smaller or same worktime but smaller index
    if l_child < len(worker_array) and ( (worker_array[l_child].worktime < worker_array[first_prior_index].worktime) or
                                        (worker_array[l_child].worktime == worker_array[first_prior_index].worktime and worker_array[l_child].id < worker_array[first_prior_index].id) ):
        first_prior_index = l_child
    if r_child < len(worker_array) and ( (worker_array[r_child].worktime < worker_array[first_prior_index].worktime) or
                                        (worker_array[r_child].worktime == worker_array[first_prior_index].worktime and worker_array[r_child].id < worker_array[first_prior_index].id) ):
        first_prior_index = r_child
    if i != first_prior_index:  # need to sift down, exchange with smaller
        temp = worker_array[i]
        worker_array[i] = worker_array[first_prior_index]  # move to top/root
        worker_array[first_prior_index] = temp
        sift_down_worker(worker_array, first_prior_index)


def my_assign_jobs(n_workers, jobs):
    res = []
    worker_array = [Worker(i) for i in range(n_workers)]
    for job in jobs:
        worker = worker_array[0]  # pop the top priority worker, based on release time, worker index, this worker will start working
        res.append(AssignedJob(worker.id, worker.worktime))  # which worker, when that worker starts working
        worker.worktime += job  # add this job process time to this worker
        sift_down_worker(worker_array, 0)  # sift down this root worker after adding work time
    return res


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = my_assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
