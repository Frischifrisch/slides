import time

start = time.time()
print(f"hello {str(start)}")

time.sleep(3.5)

end = time.time()
print(f"world {str(end)}")
print(f"Elapsed time:{str(end - start)}")
