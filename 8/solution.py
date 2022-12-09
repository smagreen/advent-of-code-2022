from itertools import product, takewhile

def read_input(filename):
    with open(filename) as f:
        lines = [list(map(int, line.strip())) for line in f.readlines()]
    return lines


def calc_view_distance(tree_height, view):
    distance = len(list(takewhile(lambda x: x < tree_height, view)))
    return distance if distance == len(view) else distance + 1


def calc_scenic_score(tree_height, left, right, up, down):
    view_left = calc_view_distance(tree_height, left)
    view_right = calc_view_distance(tree_height, right)
    view_up = calc_view_distance(tree_height, up)
    view_down = calc_view_distance(tree_height, down)

    return view_left * view_right * view_up * view_down


def find_visible_trees(forest):
    visible_trees = {}
    forest_size = len(forest[0])
    max_score = -1

    for row, col in product(range(0, forest_size), repeat=2):
        tree_height = forest[row][col]
        
        look_left = forest[row][0 : col][::-1]
        look_right = forest[row][col+1:]

        look_up = [forest[x][col] for x in range(row -1, -1, -1)]
        look_down = [forest[x][col] for x in range(row + 1, forest_size)]

        visible = False
        if tree_height > max(look_left, default=-1): visible = True
        if tree_height > max(look_right, default=-1): visible = True
        if tree_height > max(look_up, default=-1): visible = True
        if tree_height > max(look_down, default=-1): visible = True
            
        if visible: visible_trees[(row,col)] = tree_height

        scenic_score = calc_scenic_score(tree_height, look_left, look_right, look_up, look_down)
        max_score = scenic_score if scenic_score > max_score else max_score

    return len(visible_trees), max_score

visible, max_score = find_visible_trees(read_input('./8/test.txt'))
print(f"Test Part 1= {visible}, Pass={visible==21}")
print(f"Test Part 2 = {max_score}, Pass={max_score==8}")

visible, max_score = find_visible_trees(read_input('./8/input.txt'))
print(f"Part 1 = {visible}, Pass={visible==1533}")
print(f"Part 2 = {max_score}, Pass={max_score==345744}")

