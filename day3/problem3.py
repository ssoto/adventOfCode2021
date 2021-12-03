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
    binary_result = '0b'
    for element in lists_of_dicts:
        if element[0] > element[1]:
            binary_result += '0'
        else:
            binary_result += '1'
    return binary_result


def less_common(lists_of_dicts):
    binary_result = '0b'
    for element in lists_of_dicts:
        if element[0] < element[1]:
            binary_result += '0'
        else:
            binary_result += '1'
    return binary_result


def binary_to_decimal(binary: str):
    return int(binary, base=2)


def part1():
    input = read_input()
    nice_input = transmute_input(input)
    frecuencies_list_of_dicts = count_1_and_0(nice_input)
    binary_gamma_rate = most_common(frecuencies_list_of_dicts)
    binary_epsilon_rate = less_common(frecuencies_list_of_dicts)

    return binary_to_decimal(binary_gamma_rate) * binary_to_decimal(binary_epsilon_rate)


if __name__ == "__main__":
    power_consumption = part1()
    print(f'Compsution is {power_consumption}')
