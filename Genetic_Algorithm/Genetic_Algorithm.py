import time, random
from Keyboard import evaluate

# Get test data
with open("Test.txt", "r") as fh:
    test = ''.join(fh.read().splitlines()).lower()
    
# Evaluation function
def evaluate_keyboard(keyboard):
    keyboard = ''.join(keyboard)
    keyboard = [keyboard[:10], keyboard[10:20], keyboard[20:30]]  # Modify keyboard for distance calculations
    return evaluate(keyboard, test) # Return distance score

# Generate initial random population
def generate_random_keyboard():
    keys = "qwertyuiopasdfghjkl;zxcvbnm,.?" # QWERTY
    return ''.join(random.sample(keys, 30)) # Return random keyboard

def initial_population(population_size):
    return [generate_random_keyboard() for x in range(population_size)]

# Create the next generation
def new_generation(population, p_size):
    new_gen = []
    
    # Sort population by scores
    sorted_population = sorted(population, key=lambda x: evaluate_keyboard(x))
        
    # Elitism of 10%
    new_gen.extend(sorted_population[:int(p_size*0.1)])
        
    # Combine and mutate keyboards
    for _ in range(int(p_size*0.9)):
        keyboard1 = random.choice(sorted_population[:int(p_size*0.5)])
        keyboard2 = random.choice(sorted_population[:int(p_size*0.5)])
        child = mate(keyboard1,keyboard2)
        new_gen.append(child)
        
    best_score = evaluate_keyboard(sorted_population[0]) # Get best score of the generation
    return new_gen, (sorted_population[0],best_score)

def mate(board1, board2):
    idx = random.randint(0,29) # Random start index
    length = random.randint(0,29) # Random number of keys from board #1
    child = ['_' for _ in range(30)]

    for i in range(length):
        child[idx] = board1[idx]
        idx = (idx + 1) % 30 # Wrap around to zero

    child_idx = idx
    while '_' in child:
        if board2[idx] not in child:
            child[child_idx] = board2[idx]
            child_idx = (child_idx + 1) % 30
        idx = (idx + 1) % 30
        
    # 10% chance to swap two keys
    if random.random() <= 0.1:
        keypos1, keypos2 = random.sample(range(30), 2)
        child[keypos1], child[keypos2] = child[keypos2], child[keypos1]

    return ''.join(child)

if __name__ == '__main__':
    generations = 330
    population_size = 5000
    
    best_score = float('inf')
    best_keyboard = None
    starttime = time.time()

    keyboards = initial_population(population_size)
    for x in range(generations):
        print(f"*** Running generation {str(x)} ***\n")
        keyboards, best = new_generation(keyboards,population_size)
        print(f"Best of gen {str(x)}:")
        print("-"*10)
        print(f"Keyboard: {best[0]}")
        print(f"Score: {best[1]}\n\n")
        
        if best[1] < best_score:
            best_keyboard, best_score = best
    
    print("Minimum score:", best_score)
    print("Best Keyboard:\n")
    for x in [best_keyboard[:10], best_keyboard[10:20], best_keyboard[20:30]]:
        print(x)
    print(f"\nTime taken to run {str(generations)} generations: {time.time()-starttime}s")
