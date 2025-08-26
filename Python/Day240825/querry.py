from multiprocessing import Process, Queue
import time
import random


def product_worker(queue):
    for i in range(5):
        item = random.randint(1, 100)
        print(f" producer: gui du lieu {item} vao hang doi.")
        queue.put(item)
        time.sleep(random.uniform(0.1, 0.5))
    print("producer: gui tin hieu dung va ket thuc")
    queue.put(None)
def consumer_worker(queue):
    while True:
        item = queue.get()
        if item is None:
            print("consumer: nhan tin hieu dung va ket thuc.")
            break
        print(f"consumer: nhan duoc tin hieu {item}. đang xử lý...")
        time.sleep(random.uniform(0.5, 1.0))
        print(f"consumer: da xu ly xong {item}.")

if __name__ == "__main__":
    shared_queue = Queue()
    producer_process = Process(target=product_worker, args=(shared_queue,))
    consumer_process =  Process(target=product_worker, args=(shared_queue,))
    producer_process.start()
    consumer_process.start()
    producer_process.join()
    consumer_process.join()
    print("finished")