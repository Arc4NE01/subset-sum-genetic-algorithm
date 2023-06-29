# subset-sum-genetic-algorithm
This is an attempt to solve the subset sum problem using a genetic algorithm in Python.
The input file begins with two numbers, N and T, representing the count of available player and the target score, respectively. After that, there are N lines, each starting with the name of a players followed by a number R indicating the player's average score.
The output includes a row with a list of players, and the next row consists of a binary string. In the binary string, "1" represents the selected players, and "0" represents the players not selected. The sum of average scores of the selected players in the string equals the target value. If it is not possible to form such a string, the value will be -1.

Input- 
8 220
A 62
B 34
C 20
D 63
E 31
F 67
G 53
H 17

Output- 
['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
00110111

Here, the sum of the average scores of C, D, F, G and H adds up to 220.
