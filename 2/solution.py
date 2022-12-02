# A Rock, B Paper, C Scissors
# X Rock, Y Paper, Z Scissors

values = {'X':1, 'Y':2, 'Z':3}

def read_input(filename):
    return [line.strip() for line in open(filename)]

def part_1(strategy):
    wins = ['A Y','B Z','C X']
    draws = ['A X','B Y','C Z']
    scores = []
    for round in strategy:
        score = values[round[2]]
        if round in draws: score += 3
        if round in wins: score += 6
        scores.append(score)
    
    return sum(scores)

    
def part_2(strategy):
    outcomes = {'X':0, 'Y':3, 'Z':6}
    convert = {'A': 'X', 'B': 'Y', 'C': 'Z'}
    losses = {'A': 'Z', 'B': 'X', 'C': 'Y'}
    winners = {'A': 'Y', 'B': 'Z', 'C': 'X'}
    scores = []

    for round in strategy:
        opponent = round[0]
        score = outcomes[round[2]]
        match score:
            case 0:
                score += values[losses[opponent]]
            case 3:
                score += values[convert[opponent]]
            case 6:
                score += values[winners[opponent]]
        
        scores.append(score)
    
    return sum(scores)

test_data = ['A Y','B X', 'C Z']
input = read_input('./2/input.txt')

print(f"Test Part 1 = { part_1(test_data) == 15 }") #15
print(f"Solve Part 1 = { part_1(input) == 12586 }") #12586
print(f"Test Part 2 = { part_2(test_data) == 12  }") #12
print(f"Solve Part 2 = { part_2(input) == 13193 }") #13193
