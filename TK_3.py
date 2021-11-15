


def div_list(array: list) -> list:
    if not isinstance(array, (list, tuple)):
        return None
    divs = []
    avg = sum(array)/len(array)
    for i in range(len(array)):
        divs.append(i/avg)
    return divs
