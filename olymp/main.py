#  по принципу решета эратосфена, считает количество делитей у большого количества чисел
# nums = [1, 2, 4, 6, 7560, 12, 1680, 15120, 55440, 24, 36, 48, 5040, 45360, 180, 60,
#         20160, 840, 27720, 720, 2520, 83160, 10080, 50400, 360, 1260, 240, 25200, 120]
# nums.sort()
factors = [0] * 10**7
for i in range(1, 10**7+1):
    for idx in range(0, len(factors), i):
        factors[idx] += 1
print(factors)


def test(n):
    i = 1
    result = 0
    max_factors = 0
    while i <= n:
        if factors[i] > max_factors:
            max_factors = factors[i]
            result = i
        i += 1
    return result

# def test(n):
#     result = 0
#     for num in factors:
#         if num <= n:
#             result = max(num, result)
#     return result
#


if __name__ == "__main__":
    peak_factors = set()
    for i in range(1, 10**7):
        peak_factors.add(test(i))
    print(peak_factors)
