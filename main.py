import queue
import threading


def collatz_steps(n, lock):
    with lock:
        steps = 0
        while n > 1:
            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            steps += 1
        global total_steps
        total_steps += steps


# Функція для обчислення кількості кроків для чисел з черги
def process_numbers(q, lock):
    for _ in range(q.qsize()):
        try:
            number = q.get(block=False)
            collatz_steps(number, lock)
            q.task_done()
        except queue.Empty:
            break


num_threads = 4

N = 1000
numbers_queue = queue.Queue()
for i in range(1, N + 1):
    numbers_queue.put(i)

total_steps = 0
lock = threading.Lock()

threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=process_numbers, args=(numbers_queue, lock))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

average_steps = total_steps / N

print(f"Середня кількість кроків для виродження в 1: {average_steps}")

