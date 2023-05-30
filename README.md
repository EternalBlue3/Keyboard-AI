# Keyboard-AI

This code in this repository is based off of this video: https://www.youtube.com/watch?v=EOaPb9wrgDY

I started with a brute force approach of generating millions of permutations of the QWERTY keyboard to see if I could find the best one. Some quick math shows that this is not feasible as there are 30! permutations of the QWERTY keyboard. Instead, I decided to take the keyboard from Adumb's video (RSTLNE), and generate permutations of that. Here is the output of the brute force program after the first 2 million permutations:
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
While I successfully found a better keyboard, I still wanted to develop my own genetic algorithm. This led to a two stage plan.

The plan:
- Use genetic algorithm to find very good keyboard (like RSTLNE)
- Use permutations brute force to optimize the bottom row by looking at the first 10! permutations

By combining these strategies, I should be able to independently find a better keyboard than either RSTLNE, or the one I found by brute forcing permutations of the RSTLNE keyboard.

The results:
- I will put the results here as soon as I finish the programming and running of the algorithms
