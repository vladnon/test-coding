def test(num1: int, num2: int) -> int:
    nums = [num for num in range(
        min(num1, num2), max(num1, num2) + 1) if num % 7 != 0]
    return sum(nums)


if __name__ == "__main__":
    print(test(int(input()), int(input())))
