import math
from itertools import permutations, islice
from Keyboard import evaluate

with open("Test.txt", "r") as fh:
    test = ''.join(fh.readlines()).replace('\n', '').lower()
    fh.close()


default = "qwertyuiopasdfghjkl;zxcvbnm,.?" # QWERTY
minscore = math.inf
best_keyboard = default
iterations = 100000

for keyboard in islice(permutations(default), iterations):
    keyboard = ''.join(keyboard)
    keyboard = [keyboard[:10], keyboard[10:20], keyboard[20:30]]  # Modify keyboard for distance calculations
    score = evaluate(keyboard, test)

    if score < minscore:
        minscore = score
        best_keyboard = keyboard

print(best_keyboard)
print("\nScore:",minscore)
