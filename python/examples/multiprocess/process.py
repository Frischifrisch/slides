import multiprocessing as mp
import os

def func():
    print(f"proc pid: {os.getpid()} parent pid: {os.getppid()}")

def main():
    print(f"main pid: {os.getpid()} before")
    proc = mp.Process(target=func)
    proc.start()
    proc.join()
    print(f"main pid: {os.getpid()} after")


if __name__ == '__main__':
    main()

