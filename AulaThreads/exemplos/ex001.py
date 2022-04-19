import threading
import time


def worker(message):
    for i in range(5):
        print(message)
        time.sleep(1)


t = threading.Thread(target=worker, args=("Thread sendo executada",))
t.start()

while t.is_alive():
    print("Aguardando thread")
    time.sleep(1)

print("Thread morreu")
print("Finalizando programa")