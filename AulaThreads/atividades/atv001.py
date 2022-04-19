# 1. Escrever um script “hello, world” multi-threaded. Cada thread deve exibir a
# mensagem padrão com uma personalização (id da thread, parâmetro passado
# na criação, data/hora, etc).

import logging
import threading
import time


def message(nome):
    time.sleep(1)
    logging.info(f'Thread {nome} disse: Hello World!')


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%m-%d %H:%M:%S")

    threads = list()
    for num_thread in range(3):
        logging.info("Main : cria e inicializa thread %d.", num_thread)
        thr = threading.Thread(target=message, args=(num_thread,))
        threads.append(thr)
        thr.start()
        thr.join()

    logging.info('Falou my friend >_<')
