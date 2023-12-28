import threading
import time

from typing import List

keep_running = True
NUM_THREADS = 5


def dummy_thread(id: int):
    print(f'Thread {id} started. ✅')
    if id== 3:
        while True:
            time.sleep(1)
    print(f'Thread {id} stopped. ✋')


if __name__ == '__main__':
    threads: List[threading.Thread] = []
    for i in range(NUM_THREADS):
        threads.append(threading.Thread(target=dummy_thread, daemon=True, args=(i,), name=f'thread-{i}'))
    for thread in threads:
        thread.start()
    print('All threads started. 🚀')
    for thread in threads:
        thread.join()
    print('All threads finished. 🏁')