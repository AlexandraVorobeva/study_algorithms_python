def minimum_sum(self, num: int) -> int:
    num = str(num)
    num2 = []
    for nu in num:
        num2.append(nu)
    num2.sort()
    return int(num2[0] + num2[2]) + int(num2[1] + num2[3])