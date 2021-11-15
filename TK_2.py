

def min_max(array: list) -> tuple:
    if not isinstance(array, (list, tuple)):
        return None
    return (min(array), max(array))
