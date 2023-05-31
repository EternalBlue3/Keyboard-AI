import time
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

default = "qwertyuiopasdfghjkl;zxcvbnm,.?"  # QWERTY
rstlne = "qwdfz;ukypaserlhniotgxcv?bjm,."
best = "qwdfz;ukypaserlhniotxc.m?bv,jg"

# You can use these to save progress from previous brute forces or start at a specific index
iterations = 2000000
start_index = 0

# Print statistics of QWERTY keyboard
print("-"*45)
print(f"QWERTY keyboard:\n    Keyboard: {[default[:10], default[10:20], default[20:30]]}\n    Score: {evaluate_keyboard(default)}")
print("-"*45)
print(f"RSTLNE keyboard:\n    Keyboard: {[rstlne[:10], rstlne[10:20], rstlne[20:30]]}\n    Score: {evaluate_keyboard(rstlne)}")
print("-"*45)
print(f"Best keyboard found with this algorithm:\n    Keyboard: {[best[:10], best[10:20], best[20:30]]}\n    Score: {evaluate_keyboard(best)}")
print("-"*45)

if __name__ == '__main__':
    start = time.time()

    # Modify number of processes to match your number of cpu cores
    pool = Pool(processes=2)

    # Generate all permutations and skip the first 'start_index' permutations
    keyboard_permutations = islice(permutations(rstlne), start_index, start_index + iterations)

    scores = pool.map(evaluate_keyboard, keyboard_permutations)

    # Find the minimum score and corresponding keyboard
    minscore = min(scores)
    minscore_index = scores.index(minscore)
    best_keyboard = ''.join(list(islice(permutations(rstlne), start_index + iterations))[minscore_index])
    best_keyboard = [best_keyboard[:10], best_keyboard[10:20], best_keyboard[20:30]]

    print(f"Best keyboard found during search:\n    Keyboard: {best_keyboard}\n    Score: {minscore}\n    Time to calculate: {time.time()-start}s")
    print("-"*45)
