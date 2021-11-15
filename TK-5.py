

def sqrt_list(array: list) -> list:
    if not isinstance(array, (list, tuple)):
        return None
    sqrts = []
    avg = sum(array)/len(array)
    for i in range(len(array)):
        sqrts.append(i**2)
    return sqrts
