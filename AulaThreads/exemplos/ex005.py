import concurrent.futures
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    future1 = executor.submit(pow, 2, 3)
    future2 = executor.submit(pow, 5, 8)
    print(future1.result(), future2.result())