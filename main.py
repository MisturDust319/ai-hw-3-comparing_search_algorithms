import eight_puzzle
from search import iterative_deepening_search, astar_search
from math import floor
problem = eight_puzzle.EightPuzzleProblem()
# problem = EightPuzzle((0, 1, 2, 3, 4, 5, 6, 7, 8))
# print(depth_limited_search(problem))

def manhattan_distance(state):
    side_length = len(state)
    # find the length of the side of the puzzle

    distance = 0
    # the manhattan distance
    for i in range(side_length):
        for j in range(side_length):
            piece = state[i][j]
            if piece != 0:
                # find the intended row and column of the current piece
                original_row = floor((piece-1)/side_length)
                original_column = (piece-1) % side_length

                # add the current manhattan distance to a cumulative value
                distance += abs(i - original_row) + abs(j - original_column)
    return distance

def print_path(node):
    if node.parent:
        print_path(node.parent)
    print("Step: " + str(node.depth + 1))
    print(node.state[0])
    print(node.state[1])
    print(node.state[2])

print_path(astar_search(problem, lambda n: manhattan_distance(n.state)))
# print_path(iterative_deepening_search(problem))
# print(iterative_deepening_search(problem))