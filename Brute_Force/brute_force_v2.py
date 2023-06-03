import time, math
from itertools import permutations, islice
from multiprocessing import Pool
from Keyboard import evaluate

# Get test data
with open("Test.txt", "r") as fh:
    test = ''.join(fh.readlines()).replace('\n', '').lower()
    fh.close()

# Define the evaluate function
def evaluate_keyboard(keyboard):
    keyboard = ''.join(keyboard)
    keyboard = [keyboard[:10], keyboard[10:20], keyboard[20:30]]  # Modify keyboard for distance calculations
    return evaluate(keyboard, test) # Return distance score

keyboard = "yumpj;gl,daonihcsretqxfz?bvw.k" # Keyboard found with genetic algorithm

# You can use these to save progress from previous brute forces or start at a specific index
iterations = math.factorial(10)
start_index = 0

if __name__ == '__main__':
    start = time.time()

    # Modify number of processes to match your number of cpu cores
    pool = Pool(processes=2)

    # Generate all permutations and skip the first 'start_index' permutations
    keyboard_permutations = islice(permutations(keyboard), start_index, start_index + iterations)

    scores = pool.map(evaluate_keyboard, keyboard_permutations)

    # Find the minimum score and corresponding keyboard
    minscore = min(scores)
    minscore_index = scores.index(minscore)
    best_keyboard = ''.join(list(islice(permutations(keyboard), start_index, start_index + iterations))[minscore_index])
    best_keyboard = [best_keyboard[:10], best_keyboard[10:20], best_keyboard[20:30]]

    print(f"Best keyboard found during search:\n    Keyboard: {best_keyboard}\n    Score: {minscore}\n    Time to calculate: {time.time()-start}s")
    print("-"*45)
