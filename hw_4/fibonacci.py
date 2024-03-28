import threading
import time
from multiprocessing import Pool
from functools import lru_cache
from queue import Queue


@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def synchronous_execution(n, repeats=10):
    times = []
    for _ in range(repeats):
        start_time = time.time()
        fibonacci(n)
        times.append(time.time() - start_time)
    return sum(times) / len(times)


def run_threading(n, repeats=10):
    def thread_worker(n, queue):
        start_time = time.time()
        fibonacci(n)
        end_time = time.time()
        queue.put(end_time - start_time)

    threads = []
    times = Queue()

    for _ in range(repeats):
        thread = threading.Thread(target=thread_worker, args=(n, times))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_time = 0
    while not times.empty():
        total_time += times.get()

    return total_time / repeats


def measure_time_process(n):
    start_time = time.time()
    fibonacci(n)
    return time.time() - start_time


def run_multiprocessing(n, repeats=10):
    with Pool(processes=repeats) as pool:
        times = pool.map(measure_time_process, [n] * repeats)
    return sum(times) / len(times)


if __name__ == '__main__':
    n = 350
    results = [
        f"Synchronous execution time: {synchronous_execution(n)} seconds",
        f"Average threading time: {run_threading(n)} seconds",
        f"Average multiprocessing time: {run_multiprocessing(n)} seconds"
    ]

    with open('hw_4/artifacts/4.1/execution_times.txt', 'w') as file:
        for result in results:
            print(result)
            file.write(result + '\n')
