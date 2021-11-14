def mul_list(array: list) -> list:
    muls = []
    avg = sum(array)/len(array)
    for i in range(array):
        muls.append(i*avg)
    return muls
