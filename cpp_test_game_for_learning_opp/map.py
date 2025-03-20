
map: list[list[str]] = [["#"] * 10, ['#'] * 10]
columns = len(map[0])
lines = len(map)


def convert_to_string(array: list[str]) -> str:
    result = " | "
    for char in array:
        result += char
        result += " | "
    return result


def updateMap():
    map[lines // 2][columns // 2] = "z"


for col in range(columns):
    for line in range(lines):
        print(convert_to_string(map[line]))
