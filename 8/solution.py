import itertools

def read_input(filename):
    with open(filename) as f:
        lines = [list(map(int, line.strip())) for line in f.readlines()]
    return lines

def find_visible_trees(forest):
    visible_trees = {}
    forest_size = len(forest[0])

    for row, col in itertools.product(range(0, forest_size), repeat=2):
        tree_height = forest[row][col]
        
        look_left = forest[row][0 : col]
        look_right = forest[row][col+1:]

        look_up = [forest[x][col] for x in range(row -1, -1, -1)]
        look_down = [forest[x][col] for x in range(row + 1, forest_size)]

        visible = False
        if tree_height > max(look_left, default=-1): visible = True
        if tree_height > max(look_right, default=-1): visible = True
        if tree_height > max(look_up, default=-1): visible = True
        if tree_height > max(look_down, default=-1): visible = True
            
        if visible: visible_trees[(row,col)] = tree_height

    return visible_trees


def part_1(forest):
    visible = find_visible_trees(forest)
    return len(visible)

test_forest = read_input('./8/test.txt')
part_1_test = part_1(test_forest)
print(f"Test = {part_1_test}, Pass={part_1_test==21}")

forest = read_input('./8/input.txt')
part_1 = part_1(forest)
print(f"Test = {part_1}, Pass={part_1==1533}")

