#!/usr/bin/env python
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def load_file(file_name="input.txt"):
    content = []
    file_path = os.path.join(BASE_DIR, file_name)
    with open(file_path) as fd:
        for line in fd.readlines():
            stripped = line.strip()
            try:
                int_stripper = int(stripped)
            except ValueError:
                print("Can\'t parse %s", stripped)
            else:
                content.append(int_stripper)
        return content


def calculate_diffs(meassures):
    diffs = []
    for i in range(len(meassures)):
        if i == 0:
            diffs.append(0)
        else:
            diffs.append(meassures[i] - meassures[i-1])

    return diffs


def f1():
    meassures = load_file()
    meassures_diff = calculate_diffs(meassures)
    increases_tuple = [1 if x > 0 else 0 for x in meassures_diff]
    increases = sum(increases_tuple)
    print(increases)


##############

def sum_3(elements, index):
    try:
        sum_of_3 = elements[index] + elements[index+1] + elements[index+2]
    except Exception as e:
        raise
    else:
        return sum_of_3


def calculate_diffs_windows(meassures):
    result = []
    for i in range(len(meassures) - 3):
        a = sum_3(meassures, i)
        b = sum_3(meassures, i+1)
        if b - a > 0:
            result.append(1)
        else:
            result.append(0)

    return result


def f2():
    meassures = load_file()
    return calculate_diffs_windows(meassures)


if __name__ == "__main__":
    # f1()
    result = f2()
    increases = sum(result)
    print(f"There are {increases} increasing measures")
