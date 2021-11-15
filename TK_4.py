
def mul_list(array: list) -> list:
    if not isinstance(array, (list, tuple)):
        return None
    muls = []
    avg = sum(array)/len(array)
    for i in range(len(array)):
        muls.append(i*avg)
    return muls
