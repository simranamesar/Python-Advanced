import threading
import time


def thread_1(event):
    print("thread 1 started")
    time.sleep(2)
    while not event.is_set():
        set = event.wait(1)
        if set:
            print("event is set reacting to event")
        else:
            print("continue doing my work")
            # break
    # event.wait(1)
    print("event is fired for t1")
    print("thread 1 completed")


def thread_2(event):
    print("thread 2 started")
    time.sleep(3)
    event.wait(1)
    print("event is fired for t2")
    print("thread 2 completed")


start = time.strftime("%X")
# thread_1()
# thread_2()
e = threading.Event()

t1 = threading.Thread(name="t1", target=thread_1, args=(e,))
t2 = threading.Thread(name="t2", target=thread_2, args=(e,))
# t1.daemon = True
t1.start()
t2.start()
time.sleep(6)
e.set()

print("main thread continues")
# t1.join()
# t2.join()
print(f'started at {start} and ended at {time.strftime("%X")}')
