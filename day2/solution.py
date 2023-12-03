import re

with open("input.txt", "r") as f:
    games = f.readlines()

_COLOR = ["red", "green", "blue"]


def check(reality, to_check):
    for color, nums in reality.items():
        if not to_check[color] <= nums:
            return False

    return True


def find_colors(text):
    result = {c: 0 for c in _COLOR}
    for color in result:
        result[color] = int(
            find_num_and_strip_str(re.compile(r"(\d+) ({})".format(color)), text)
        )
    return result


def find_num_and_strip_str(pattern, text):
    m = pattern.search(text)
    if m is None:
        return 0
    g = m.group()
    [result] = [i for i in g.split(" ") if i.isdigit()]
    return result


def solution_1(total):
    result = 0
    for game in games:
        gid = find_num_and_strip_str(re.compile(r"Game \d+"), game)
        sub_games = game.split(":")[1].split(";")
        sub_result = True
        for sg in sub_games:
            cubes_in_colors = find_colors(sg)
            if not check(total, cubes_in_colors):
                sub_result = False
                break
        if sub_result:
            result += int(gid)

    return result


def solution_2():
    result = 0
    for game in games:
        sub_games = game.split(":")[1].split(";")
        biggest = {c: 0 for c in _COLOR}
        for sg in sub_games:
            cubes_in_colors = find_colors(sg)
            for color, cube in cubes_in_colors.items():
                if cube > biggest[color]:
                    biggest[color] = cube
        tmp = 1
        for v in biggest.values():
            tmp *= v
        result += tmp

    return result


if __name__ == "__main__":
    question = "12 red cubes, 13 green cubes, and 14 blue cubes"
    result = solution_1({"red": 12, "green": 13, "blue": 14})
    print(result)
    result = solution_2()
    print(result)
