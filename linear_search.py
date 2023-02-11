

def search(num_list: list, target: int) -> int:
    n: int = 0
    for i in num_list:
        n += 1
        if i == target:
            return n
    return n