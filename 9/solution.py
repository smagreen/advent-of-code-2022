import math

VECTORS = {
        'N':(0,1), 'NE':(1,1), 'E':(1,0), 'SE':(1,-1),
        'S':(0,-1), 'SW':(-1,-1), 'W':(-1,0), 'NW':(-1,1)}

def read_input(filename):
    with open(filename) as f:
        lines = [line.strip().split() for line in f.readlines()]
    return lines

def get_direction(head, tail):
    hx, hy = head
    tx, ty = tail

    dx = hx - tx
    dy = hy- ty

    degrees_temp = math.atan2(dx, dy)/math.pi*180
    degrees_final = degrees_temp if degrees_temp > 0 else 360 + degrees_temp
    compass = ["N", "NE", "E", "SE", "S", "SW", "W", "NW", "N"]
    compass_lookup = round(degrees_final / 45)

    return compass[compass_lookup]

def move_tail(head, tail):
    hx, hy = head
    tx, ty = tail

    dx = abs(hx - tx)
    dy = abs(hy- ty)

    if dx < 2 and dy < 2: return tail

    direction = get_direction(head, tail)
    vector = VECTORS[direction]
    new_tail = tuple(map(sum, zip(tail, vector)))
   
    return (new_tail)

def run(instructions, rope_length=1):
    positions = [(0,0)] * rope_length
    moves = {'R':(1,0), 'L':(-1,0), 'U':(0,1), 'D':(0,-1)}
    points_visited = set()

    for direction, distance in instructions:
        move = moves[direction]
        for _ in range(0, int(distance)):
            positions[0] = tuple(map(sum, zip(positions[0], move)))
            for idx in range(0, len(positions)):
                if idx > 0:
                    positions[idx] = move_tail(positions[idx-1], positions[idx])
            
            points_visited.add(positions[-1])
   
    return len(points_visited)

instructions = read_input('./9/input.txt')
part_1 = run(instructions, 2)
part_2 = run(instructions, 10)
print(f"Solve Part 1 = {part_1}, Pass={part_1==6190}")
print(f"Solve Part 2 = {part_2}, Pass={part_2==2516}")
