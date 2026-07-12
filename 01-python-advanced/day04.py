
import threading
import time

def worker(name):
    for i in range(5):
        print(f"{name}: {i}")
        time.sleep(1)

t1 = threading.Thread(target=worker, args=("Thread-1",))
t2 = threading.Thread(target=worker, args=("Thread-2",))

t1.start()
t2.start()

t1.join()
t2.join()
