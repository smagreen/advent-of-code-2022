import heapq
from itertools import product
import logging
import time

logging.basicConfig(level=logging.DEBUG, filename="./12/12.log", filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s")

def read_input(filename):
    with open(filename) as f:
        lines = [list(line.strip()) for line in f.readlines()]

    return lines

def build_graph(lines):
    start_time = time.perf_counter()
    graph = {}
    start, end = None, None
    num_rows, num_cols = len(lines), len(lines[0])
    
    # possible directions
    adjacents = [(0,-1), (0,1), (-1,0), (1,0)]
    # all combinations of x,y coords
    grid = list(product(range(len(lines)), range(len(lines[0]))))

    # find coords of start and end points
    for row, col in grid:
        if lines[row][col] == "S": start = (row, col)
        if lines[row][col] == "E": end = (row, col)

    # build Graph/Dictionary of edge weights
    for row, col in grid:
        graph[(row, col)] = {}
        current = lines[row][col]
        if current == 'S': current = 'a'

        for dy, dx in adjacents:
            ar, ac = (row + dy, col + dx)
            if 0 <= ar < num_rows and 0 <= ac < num_cols:
                # if adjacent cell is the END and we aren't at z, we can't finish
                cost = 99
                if ((ar, ac) == end):
                    if current == 'z': cost = 1        
                else:
                    cost = ord(lines[ar][ac]) - ord(current)
                if cost <= 1: 
                        graph[(row, col)].update({(ar,ac): 1})                        

    end_time = time.perf_counter()
    logging.info(f"Graph generated: {start}, End: {end} - Time: {end_time - start_time:0.4f} secs ")

    return graph, start, end

def part_1(lines):
    logging.info(f"=== Part 1, Rows: {len(lines)} , Cols: {len(lines[0])} ===")
    graph, start, end = build_graph(lines)
    end_time = time.perf_counter()

    start_time = time.perf_counter()
    shortest_distance = run_dijkstra(graph, start, end)
    end_time = time.perf_counter()
    logging.info(f"Shortest Path: {shortest_distance} - Time: {end_time - start_time:0.4f} secs ")

    return shortest_distance


def part_2(lines):
    logging.info(f"=== Part 2, Rows: {len(lines)} , Cols: {len(lines[0])} ===")

    coords = list(product(range(len(lines)), range(len(lines[0]))))
    starts = []
    for row, col in coords:
        if lines[row][col] == 'S': lines[row][col] = 'a'
        if lines[row][col] == 'a': starts.append((row, col))

    graph, _, end = build_graph(lines)

    logging.info(f"Finding Shortest Paths for {len(starts)} starts")

    start_time = time.perf_counter()
    distances = []
    for start in starts:
        distances.append(run_dijkstra(graph, start, end))

    end_time = time.perf_counter()
    logging.info(f"{len(starts)} Paths Calculated in: {end_time - start_time:0.4f} secs ")
    
    return min(distances)


def run_dijkstra(graph, start, end):
  distances = {}
  for node in graph:
    distances[node] = float("inf")

  distances[start] = 0
  heap = [(0, start)]

  while heap:
    current_distance, current_node = heapq.heappop(heap)
    if current_node == end:
      break
    for next, edge_weight in graph[current_node].items():
      new_distance = current_distance + edge_weight
      if new_distance < distances[next]:
        distances[next] = new_distance
        heapq.heappush(heap, (new_distance, next))
  return distances[end]


test_lines = read_input('./12/test.txt')
lines = read_input('./12/input.txt')
part_1_test = part_1(test_lines)
part_1_result = part_1(lines)

print(f"{part_1_test}, { 'Pass' if 31==part_1_test else 'Fail'}")
print(f"{part_1_result}, {'Pass' if 391==part_1_result else 'Fail'}")

part_2_test = part_2(test_lines)
print(f"{part_2_test}, {'Pass' if 29==part_2_test else 'Fail'}")

part_2_result = part_2(lines)
print(f"{part_2_result}, {'Pass' if 386==part_2_result else 'Fail'}")

