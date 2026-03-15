from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args) -> Any:
        if result.get(args, False) is False:
            print("Calculating new result")
            result[args] = func(*args)
        else:
            print("Getting from cache")

        return result[args]
    return wrapper
