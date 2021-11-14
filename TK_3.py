def div_list(array: list) -> list:
    divs = []
    avg = sum(array)/len(array)
    for i in range(array):
        divs.append(i/avg)
    return divs
