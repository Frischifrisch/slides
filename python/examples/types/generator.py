from typing import Generator

def numbers(n: int) -> Generator[int, None, None]:
    return iter(range(n))

print(list(numbers(10)))
