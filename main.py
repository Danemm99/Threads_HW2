import multiprocessing

def collatz_steps(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

def compute_collatz_average(N, num_threads):
    pool = multiprocessing.Pool(num_threads)
    numbers = list(range(1, N + 1))
    results = pool.map(collatz_steps, numbers)
    pool.close()
    pool.join()
    average_steps = sum(results) / N
    return average_steps

if __name__ == '__main__':
    N = 1000
    num_threads = 4

    average_steps = compute_collatz_average(N, num_threads)
    print(f"Середня кількість кроків для чисел від 1 до {N}: {average_steps}")

