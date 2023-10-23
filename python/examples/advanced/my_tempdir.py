from contextlib import contextmanager

import time
import random
import os
import shutil


@contextmanager
def my_tempdir():
    print("start return")
    tmpdir = f'/tmp/{str(time.time())}{random.random()}'
    os.mkdir(tmpdir)
    try:
        yield tmpdir
    finally:
        shutil.rmtree(tmpdir)
        print("end return")
