import os
import pytest

print(f"DATABASE = {os.environ['DATABASE']}")

@pytest.mark.postgresql
def test_postgresql():
    print("Testing postgresql")

@pytest.mark.mysql
def test_mysql():
    print("Testing mysql")
