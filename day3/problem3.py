import os


def read_input(file_name="input.txt"):
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(cur_dir, file_name)
    with open(file_path) as fd:
        return [s.strip() for s in fd.readlines()]


def transpose_input(input):
    result = ['' for i in range(len(input[0].strip()))]
    for i in range(len(input)):
        element = input[i].strip()
        for j in range(len(element)):
            # print(f"input[{i}][{j}] -> {input[i][j]}")
            item = input[i][j]
            result[j] = f'{result[j]}{item}'
    return result


def count_1_and_0(input):
    if type(input) == str:
        result = {
            0: input.count('0'),
            1: input.count('1')
        }
    else:
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
    nice_input = transpose_input(input)
    frecuencies_list_of_dicts = count_1_and_0(nice_input)
    binary_gamma_rate = most_common(frecuencies_list_of_dicts)
    binary_epsilon_rate = less_common(frecuencies_list_of_dicts)

    return binary_to_decimal(binary_gamma_rate) * binary_to_decimal(binary_epsilon_rate)

################################
#           Part 2             #
################################


def delete_from(problem_input, zero_or_one, i):
    result = []
    for element in problem_input:
        if element[i] != zero_or_one:
            result.append(element)
    return result


def calculate_oxygen_rating(problem_input):
    for i in range(len(problem_input[0])):
        transposed_input = transpose_input(problem_input)
        frecuency_dict = count_1_and_0(transposed_input[i])
        if frecuency_dict[1] >= frecuency_dict[0]:
            # 0
            to_remove = '0'
        else:
            # 1
            to_remove = '1'
        problem_input = delete_from(problem_input, to_remove, i)
        if len(problem_input) == 1:
            return problem_input[0]


def calculate_co2_scrubber(problem_input):
    for i in range(len(problem_input[0])):
        transposed_input = transpose_input(problem_input)
        frecuency_dict = count_1_and_0(transposed_input[i])
        if frecuency_dict[0] <= frecuency_dict[1]:
            # 0
            to_remove = '1'
        else:
            # 1
            to_remove = '0'
        problem_input = delete_from(problem_input, to_remove, i)
        if len(problem_input) == 1:
            return problem_input[0]


def calculate_life_support_rating():
    problem_input = read_input()
    # problem_input = read_input("sample_input.txt")
    oxygen_rating = calculate_oxygen_rating(problem_input)
    co2_scrubber = calculate_co2_scrubber(problem_input)

    return int(oxygen_rating, base=2) * int(co2_scrubber, base=2)


if __name__ == "__main__":
    print('Part 1:')
    power_consumption = part1()
    print(f'Compsution is {power_consumption}')
    print('*' * 20)
    print('Part 2: ')
    life_support_rating = calculate_life_support_rating()
    print(f"Life support rating is {life_support_rating}")
