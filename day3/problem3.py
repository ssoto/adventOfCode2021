import os


def read_input(file_name="input.txt"):
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(cur_dir, file_name)
    with open(file_path) as fd:
        return fd.readlines()


def transmute_input(input):
    result = ['' for i in range(len(input[0].strip()))]
    for i in range(len(input)):
        element = input[i].strip()
        for j in range(len(element)):
            # print(f"input[{i}][{j}] -> {input[i][j]}")
            item = input[i][j]
            result[j] = f'{result[j]}{item}'
    return result


def count_1_and_0(input):
    result = []
    for value in input:
        result.append({
            0: value.count('0'),
            1: value.count('1')
        })
    return result


def most_common(lists_of_dicts):
    result = ''
    for element in lists_of_dicts:
        if element[0] > element[1]:
            result += '0'
        else:
            result += '1'
    return result


def part1():
    input = read_input()
    nice_input = transmute_input(input)
    result = count_1_and_0(nice_input)
    binary_gamma_rate = most_common(result)



if __name__ == "__main__":
    part1()
