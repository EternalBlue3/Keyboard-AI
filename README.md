# Keyboard-AI

This code is based off of this video: https://www.youtube.com/watch?v=EOaPb9wrgDY

This code is a brute force method to try to find the best possible keyboard. This is not feasible as there are 30! permutations to the QWERTY keyboard. I decided to be a bit smarter, and generate permutations of the RSTLNE keyboard, but this is still slow, and I will be writing my own genetic algorithm similar to the one used by Adumb in his video.

Here is the output of the program after the first 2 million permutations:
```
---------------------------------------------
QWERTY keyboard:
    Keyboard: ['qwertyuiop', 'asdfghjkl;', 'zxcvbnm,.?']
    Score: 14071.058
---------------------------------------------
RSTLNE keyboard:
    Keyboard: ['qwdfz;ukyp', 'aserlhniot', 'gxcv?bjm,.']
    Score: 6604.76
---------------------------------------------
Best keyboard found during search:
    Keyboard: ['qwdfz;ukyp', 'aserlhniot', 'xc.m?bv,jg']
    Score: 6343.03
---------------------------------------------
```
The two stage plan:
- Use genetic algorithm to find pretty good keyboard
- Use permutations brute force to optimize the bottom row by looking at the first 10! permutations
