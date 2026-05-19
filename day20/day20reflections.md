## Day 20 (AoC 2024)

## Part 1
I initially tried to simulate all possible cheats via BFS, but that ended being overly complex, where each state in the queue required several parameters such as the number of cheat moves left, whether the cheat has been activated, etc.

Since there is only one path from start to finish, there is an easier method. We know that for a cheat of 2 ps, the Manhattan distance must be 2. 

The Manhattan distance is defined as:

$d_{m} = \vert x_2 - x_1 \vert + \vert y_2 - y_1 \vert$

So, we have the following algorithm:
1. Trace from start to end once, building the path $p$  and storing the elapsed time $t$ at every move. 
2. For every $(x_i,y_i)$ in $p$, determine if any points that lie $d_m = 2$ away are also on the path $p$.
    * If true, take the difference of $(x_i, y_i) + d_m$ with $(x_i, y_i)_t$. 
    * If this difference $\geq 100$, increment the final counter.

## Part 2

The above algorithm can be generalized for part 2. 
1. Consider all possible pairs of points $(x_i, y_i), (x_j, y_j) \in p$. For a given pair, calculate $d_m$.
2. If $d_m \leq 20$, calculate $(x_i, y_i) + d_m - (x_i, y_i)_t$
    * If this difference $\geq 100$, increment the final counter.


### Focus Points
* Manhattan distance
* Thinking about shortcuts rather than just jumping to BFS
