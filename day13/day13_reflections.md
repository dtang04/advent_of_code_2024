## Day 13 (AoC 2024)

This problem was solved with the key realization that the number of button presses for each game could be broken down into a system of equations:


$a_1X_1 + a_2X_2 = P_1$

$a_1Y_1 + a_2Y_1 = P_2$

Here, $X_1$ is how much one press of button 1 moves us in the x direction. $Y_1$ is how much one press of button 2 moves is in the y direction. The same holds for $X_2$, $Y_2$, just for button 2.

Then, $a_1$, $a_2$ is the number of button presses for buttons 1 and 2 respectively to reach $P_1$ and $P_2$

Then, we can reformulate this as $Ax = b$.

$\underbrace{\begin{bmatrix} X_1 & X_2 \\ Y_1 & Y_2 \end{bmatrix}}_A\underbrace{\begin{bmatrix} a_1 \\ a_2\end{bmatrix}}_x = \underbrace{\begin{bmatrix}P_1 \\ P_2\end{bmatrix}}_b$

Assuming A is full rank, `np.linalg.solve(A, b)` gives us the answer. We round to remove potential floating points roundoff errors, and recheck the rounded values are indeed the solutions to $Ax = b$.

Then, to finish the problem, we just return $3 * P_1 + P_2$.

---
However, if $A$ is not full rank (looking at the AoC test input, this is never the case), the system degenerates into $a_1X_1 + a_2X_2 = P_1$. Then, since each increment in $X_1$ costs $3$, and each increment in $X_2$ costs $1$, finding the optimal price becomes

$\quad \quad \min_{a_1, a_2} 3a_1X_1 + a_2X_2$ 

$\quad \text{s.t. } a_1X_1 + a_2X_2 = P_1$

satisfying $a_1Y_1 + a_2Y_2 = P_2$.

In our implementation, we approached this via brute force checking all possible $a_1, a_2$ pairs.

