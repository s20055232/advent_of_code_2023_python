import re

mapper = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def str_to_int(line: str):
    find_indexs = {}
    for k, v in mapper.items():
        results = re.finditer(k, line)
        for r in results:
            start, _ = r.span()
            find_indexs[start] = v
    return find_indexs


def calculate(line):
    front_idx = 0
    end_idx = len(line) - 1
    front = -1
    end = -1
    find_indexs = str_to_int(line)
    while front == -1 or end == -1:
        if front_idx in find_indexs:
            front = find_indexs[front_idx]
        elif line[front_idx].isdigit():
            front = int(line[front_idx])
        else:
            front_idx += 1

        if end_idx in find_indexs:
            end = find_indexs[end_idx]
        elif line[end_idx].isdigit():
            end = int(line[end_idx])
        else:
            end_idx -= 1
    return 10 * front + end


def old_calculate(line):
    front_idx = 0
    end_idx = len(line) - 1
    front = -1
    end = -1
    while front == -1 or end == -1:
        if line[front_idx].isdigit():
            front = int(line[front_idx])
        else:
            front_idx += 1

        if line[end_idx].isdigit():
            end = int(line[end_idx])
        else:
            end_idx -= 1
    return 10 * front + end


if __name__ == "__main__":
    with open("input2.txt", "r") as f:
        lines = f.read()
    result = 0
    for line in lines.splitlines():
        result += calculate(line)

    print(result)
