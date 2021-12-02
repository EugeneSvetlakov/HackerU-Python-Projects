import threading
import time
from threading import Lock


def worker(s, n):
    for i in range(n):
        # в единицу времени в эту часть блока может попасть только один поток
        with lock:
            print(s, i)
            time.sleep(2)


lock = Lock()

# t1 - запустится как демон (сервис)
# и завершается автоматически по завершении Главного потока
t1 = threading.Thread(target=worker, args=("thread 1", 10), daemon=True)
t2 = threading.Thread(target=worker, args=("thread 2", 5))
t3 = threading.Thread(target=worker, args=("thread 3", 7))
print("threads ready")
t1.start()
t2.start()
t3.start()
t2.join()  # Главный поток Подожди пока законится поток t2

print("threads started")
print("programm finishe")
