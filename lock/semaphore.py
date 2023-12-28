import threading
import time

x = 0


def increment():
    global x
    curr_x = x
    time.sleep(0.0001)
    x = curr_x + 1


def unsafe_thread_example():
    for i in range(1000):
        increment()


if __name__ == '__main__':
    t1 = threading.Thread(target=unsafe_thread_example)
    t2 = threading.Thread(target=unsafe_thread_example)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"x value: {x}")
