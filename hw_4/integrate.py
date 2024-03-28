import math
import concurrent.futures
import logging
import time
from datetime import datetime
import os
# Настройка логирования
logging.basicConfig(filename='integration_log.log',
                    level=logging.INFO, format='%(asctime)s - %(message)s')


def integrate_part(f, a, b, *, n_iter):
    """Вычисляет часть интеграла функции f на интервале [a, b]."""
    step = (b - a) / n_iter
    acc = sum(f(a + i * step) * step for i in range(n_iter))
    return acc


def integrate(f, a, b, *, n_jobs=1, n_iter=1000, executor_class=concurrent.futures.ThreadPoolExecutor):
    """Вычисляет интеграл функции f на интервале [a, b] с возможностью параллельного выполнения."""
    step = (b - a) / n_jobs
    parts = [(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
    with executor_class(max_workers=n_jobs) as executor:
        futures = [executor.submit(integrate_part, f, part_start, part_end,
                                   n_iter=n_iter // n_jobs) for part_start, part_end in parts]
        return sum(future.result() for future in futures)


def test_executor(executor_class, f, a, b, n_iter=1000, cpu_num=4):
    times = []
    for n_jobs in range(1, cpu_num * 2 + 1):
        start_time = time.time()
        integrate(f, a, b, n_jobs=n_jobs, n_iter=n_iter,
                  executor_class=executor_class)
        end_time = time.time()
        times.append((n_jobs, end_time - start_time))
        logging.info(
            f"{executor_class.__name__} with n_jobs={n_jobs}: {end_time - start_time}s")
    return times


os.cpu_count()
if __name__ == "__main__":
    cpu_num = 12  # os.cpu_count() для определения количества CPU
    times_thread = test_executor(
        concurrent.futures.ThreadPoolExecutor, math.cos, 0, math.pi / 2, cpu_num=cpu_num)
    times_process = test_executor(
        concurrent.futures.ProcessPoolExecutor, math.cos, 0, math.pi / 2, cpu_num=cpu_num)

    with open("execution_times.txt", "w") as file:
        file.write("ThreadPoolExecutor times:\n")
        for n_jobs, time_ in times_thread:
            file.write(f"{n_jobs} jobs: {time_}s\n")
        file.write("\nProcessPoolExecutor times:\n")
        for n_jobs, time_ in times_process:
            file.write(f"{n_jobs} jobs: {time_}s\n")
