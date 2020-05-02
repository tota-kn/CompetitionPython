# region
import sys

DEBUG = True if (len(sys.argv) > 1 and sys.argv[1] == "DEBUG") else False


def dp(value):
    if DEBUG:
        print(value)
    return


def input_text(split=" "):
    # 入力
    result = []
    while True:
        try:
            row = list(
                map(lambda x: int(x) if x.isdecimal() else x, input().split(split))
            )
            result.append(row)
        except EOFError:
            break
    return result


# endregion
it = input_text()
count = 0

print(count)
