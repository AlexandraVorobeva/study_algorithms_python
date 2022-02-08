# Given a positive integer, check whether it has alternating bits:
# namely, if two adjacent bits will always have different values.

def has_alternating_bits(n: int) -> bool:
    num = format(n, 'b')
    for i in range(len(num) - 1):
        if num[i] == num[i + 1]:
            return False
    return True