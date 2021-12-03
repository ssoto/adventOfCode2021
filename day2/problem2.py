import os

FORWARD = "forward"
DOWN = "down"
UP = "up"


def get_movement(step):
    [movement_type, units] = step.strip().split(" ")
    units = int(units)
    if movement_type == FORWARD:
        return [units, 0]
    elif movement_type == DOWN:
        return [0, units]
    elif movement_type == UP:
        return [0, -units]
    else:
        raise Exception(f"Unrecognized movement type {movement_type}")


def update_position(position, step):
    movement = get_movement(step)
    new_position = [
        position[0] + movement[0],
        position[1] + movement[1]
    ]
    return new_position


def manage_plan(plan):
    position = [0, 0]
    for step in plan:
        position = update_position(position, step)
    return position


def parse_plan(file_name="input.txt"):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)
    with open(file_path) as fd:
        return fd.readlines()


def part1():
    plan = parse_plan()
    final_position = manage_plan(plan)
    print(f"Final position is {plan}")
    product = final_position[0] * final_position[1]
    print(f"Final position product is {product}")


########################################################
##                    part 2                         ##
########################################################


def get_movement_with_aim(step):
    [movement_type, aim] = step.strip().split(" ")
    aim = int(aim)
    return [movement_type, aim]

def update_position_with_aim(position, step):
    """

    :param position:  [x, y, z]
    :param step: string with "down X", "up Y" or "forward Z"
    :return: new position vector [x', y', z']
    """
    movement_type, x = get_movement_with_aim(step)
    x_pos, y_pos, aim_pos = position

    if movement_type == FORWARD:
        return [
            x_pos + x,
            y_pos + (aim_pos * x),
            aim_pos
        ]
    elif movement_type == DOWN:
        return [x_pos, y_pos, aim_pos + x]
    elif movement_type == UP:
        return [x_pos, y_pos, aim_pos - x]
    else:
        raise Exception(f"Unrecognized movement type {movement_type}")


def manage_plan_with_aim(plan):
    position = [0, 0, 0]
    for step in plan:
        position = update_position_with_aim(position, step)
    return position


def part2_test_plan():
    return [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2"
    ]


def part2():
    # plan = part2_test_plan()
    plan = parse_plan()
    final_position = manage_plan_with_aim(plan)
    print(f"Final position is {final_position}")
    product = final_position[0] * final_position[1]
    print(f"Final position product is {product}")

if __name__ == "__main__":
    # part1()
    part2()
