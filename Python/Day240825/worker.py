from multiprocessing import Process
import time
import os

def worker(name):
    print(f"Process{name}(ID: {os.getpid()}) starting.")
    start_time = time.time()
    time.sleep(2)
    print(f"process {name}(ID: {os.getpid()}) finished.")

if __name__ == "__main__":
    processes= []
    # create two processes 
    p1= Process(target=worker, args=("Alpha",))
    p2= Process(target=worker, args=("Beta",))

    p1.start()
    p2.start()

    print("main process: All processes started.")

    p1.join()
    p2.join()

    print("main process: All processes finish")