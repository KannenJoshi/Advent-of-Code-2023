# Check all 50 in 25 days - 2/day - 1 star each

# c-val => combine first digit and last digit into two digit no.


### PART ONE ###
def calibrate(text: str) -> int:
    digits = [n for n in text if n.isnumeric()]
    cval = "{}{}".format(digits[0],digits[-1])
    return int(cval)


def cval_sum(file="20231201_data.txt", data=None):
    cvals = []

    if data:
        for cval in data:
            cvals.append(calibrate(cval))
    else:
        with open(file) as cdata:
            for cval in cdata:
                cvals.append(calibrate(cval))
    return sum(cvals)


### PART TWO ###
def calibrate2(text: str) -> int:
    letters = {"one": "o1e","two": "t2o","three": "t3e",
               "four": "f4r","five": "f5e","six": "s6x",
               "seven": "s7n","eight": "e8t","nine": "n9e"}

    #print(text)

    # GO BY APPEARS FIRST NOT ORDER OF LETTERS
    # for s, n in letters.items():
    #     text = text.replace(s, f"{n}")

    output = ""
    for char in text:
        output += char
        # print("1",output)
        for s, n in letters.items():
            output = output.replace(s, n)
        # print("    "+output[len(output)-2], output[len(output)-2].isnumeric())
        # print("2",output)

    # Change text to output
    digits = [n for n in output if n.isnumeric()]
    # print(digits)
    cval = "{}{}".format(digits[0],digits[-1])
    #print(text, cval)
    return int(cval)


def csum(data: list[str]) -> int:
    return sum([calibrate2(cval) for cval in data])


def part_two(file="20231201_data.txt"):
    total = 0
    with open(file) as data:
        # return csum([cval for cval in data])
        for cval in data:
            val = calibrate2(cval)
            total += val
           # print(total, val, cval)
    return total
