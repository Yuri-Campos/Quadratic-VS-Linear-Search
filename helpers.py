BASE: int = 2


def log(b):
    if(b == 1):
        return 0
    return 1 + log(b//BASE)

def list_generator(list_size: int) -> list:
    generated_list: list = []
    for i in range(0, list_size):
        generated_list.append(i)

    return generated_list