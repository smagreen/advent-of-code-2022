import solution_1

example = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_part_1():
    assert solution_1.count_larger(example) == 7


def test_part_2():
    assert solution_1.sliding_window(example) == 5
