# 2 - Fazer um script em Python que utilize múltiplas threads (5) em que cada thread
# exibe a hora atual em sequência num intervalo determinado, porém as threads
# são executadas em tempos aleatórios. Por exemplo, T1 5 segundos, T2 7
# segundos, T3 13 segundos, T4 23 segundos e T5 26 segundos. A informação
# exibida deve identificar também a Thread que está exibindo a informação.
# Utilize prints ou logs para exibir as informações.

import logging
import threading
import time


def mostrar_hora(nome, tempo):
    time.sleep(tempo)
    logging.info(f'Thread {nome} mostrou a hora: {time.time()}')


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%Y-%m-%d")
    
    thr1 = threading.Thread(target=mostrar_hora, args=("t1", 5))
    thr2 = threading.Thread(target=mostrar_hora, args=("t2", 7))
    thr3 = threading.Thread(target=mostrar_hora, args=("t3", 13))
    thr4 = threading.Thread(target=mostrar_hora, args=("t4", 23))
    thr5 = threading.Thread(target=mostrar_hora, args=("t5", 26))

    thr1.start()
    thr2.start()
    thr3.start()
    thr4.start()
    thr5.start()
