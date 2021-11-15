def sqrt_list(array: list) -> list:
    sqrts = []
    avg = sum(array)/len(array)
    for i in range(array):
        sqrts.append(i**2)
    return sqrts
