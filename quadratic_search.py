

def search(num_list: list, target: int) -> int:
    n: int = 0
    low: int = 0 
    high: int = len(num_list) - 1
    half_point: int = 0
    active_value: int = 0

    while high >= low:
        n += 1
        half_point = (high + low) // 2
        active_value = num_list[half_point]
        if half_point == target:
            return n
        elif active_value > target:
            high = half_point - 1
        else:
            low = half_point + 1
    return n