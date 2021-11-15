

def list_input(n: int):
    if not isinstance(n, int):
        return None
    array = []
    for i in range(n):
        array.append(input("list_input Insert number: "))
    return array
        