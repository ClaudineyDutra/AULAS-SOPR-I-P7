import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: iniciando", name)
    time.sleep(2)
    logging.info("Thread %s: finalizando", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO)
    logging.info("Main : antes de criar thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main : antes de rodar thread")
    x.start()
    logging.info("Main : esperando pela thread finalizar")
    x.join()
    logging.info("Main : tudo pronto")