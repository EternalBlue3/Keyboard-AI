# Keyboard-AI

This code in this repository is based off of this video: https://www.youtube.com/watch?v=EOaPb9wrgDY

I started with a brute force approach of generating millions of permutations of the QWERTY keyboard to see if I could find the best one. Some quick math shows that this is not feasible as there are 30! permutations of the QWERTY keyboard. Instead, I decided to take the keyboard from Adumb's video (RSTLNE), and generate permutations of that. The code can be found in the file "brute_force_v1.py."

Here is the output of the brute force program after the first 2 million permutations:
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

Two stage plan results:

So, step one went better than I could have hoped. Here is a truncated version of the final output of the program:
```
*** Running generation 329 ***

Best of gen 329:
----------
Keyboard: yumpj;gl,daonihcsretqxfz?bvw.k
Score: 6052.453


Minimum score: 6052.453
Best Keyboard:

yumpj;gl,d
aonihcsret
qxfz?bvw.k

Time taken to run 330 generations: 56097.44495868683s
```

The keyboard found is much better than the one found by generating permutations of the RSTLNE keyboard, and claims the throne for the best keyboard i've found so far.

Dissapointingly, the permutations algorithm, which can be found in "brute_force_v2.py" did not manage to find a better keyboard than the one found by the genetic algorithm. If you want to run any of the code found above, make sure that all files are located in the same directory.

Another thing to mention is distance isn't the only metric by which to evaluate a keyboard. I may come back in the future, and use a better evaluation function, or rewrite and optimize the code in c++, but for now I am going to focus on other projects. If you want to learn more, watch the video that this repository was based on. It is a great video and if you found this interesting, you will love the video.
