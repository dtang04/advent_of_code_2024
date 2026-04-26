import numpy as np
import math

# Part 1 Globals
A = {}
B = {}
prize = {}

# Part 2 Globals
prize_ = {}

def solveGame_P1(n_game):
    """
    Tries to get the winning number of button A moves and button B moves
    by solving the following system:

    X_1 * a1 + X_2 * a2 = P1
    Y_1 * a1 + Y_2 * a2 = P2
    """
    X_1, Y_1 = A[n_game]
    X_2, Y_2 = B[n_game]
    P_1, P_2 = prize[n_game]
    A_m = np.array([[X_1, X_2], [Y_1, Y_2]])
    b = np.array([P_1, P_2])
    try:
        sol = np.linalg.solve(A_m, b)
        a1 = round(sol[0])
        a2 = round(sol[1])
        if a1 * X_1 + a2 * X_2 == P_1 and a1 * Y_1 + a2 * Y_2 == P_2:
            return a1 * 3 + a2
        return "No Solution"
    except np.linalg.LinAlgError: # Basis vectors are parallel, infinitely many solutions or no solutions
        # Simplifies to a_1 * X_1 + a_2 * X_2 = P1
        # min 3*a_1 + a_2
        # s.t. a_1 * X_1 + a_2 * X_2 = P1
        a_1 = 0
        min_a_1 = 0
        min_a_2 = 0
        min_cost = math.inf
        while a_1 <= P_1:
            a_2 = (P_1 - a_1 * X_1) / X_2
            if a_2.is_integer(): # Valid solution
                if min_cost > 3 * a_1 + a_2 and a_1 * Y_1 + a_2 * Y_2 == P_2: # Need to check if a_1, a_2 satisfy the second equation as well
                    min_cost = 3 * a_1 + a_2
            a_1 += 1
        return min_cost

def solveGame_P2(n_game):
    """
    Tries to get the winning number of button A moves and button B moves
    by solving the following system:

    X_1 * a1 + X_2 * a2 = P1
    Y_1 * a1 + Y_2 * a2 = P2
    """
    X_1, Y_1 = A[n_game]
    X_2, Y_2 = B[n_game]
    P_1, P_2 = prize_[n_game]
    A_m = np.array([[X_1, X_2], [Y_1, Y_2]])
    b = np.array([P_1, P_2])
    try:
        sol = np.linalg.solve(A_m, b)
        a1 = round(sol[0])
        a2 = round(sol[1])
        if a1 * X_1 + a2 * X_2 == P_1 and a1 * Y_1 + a2 * Y_2 == P_2:
            return a1 * 3 + a2
        return "No Solution"
    except np.linalg.LinAlgError: # Basis vectors are parallel, infinitely many solutions or no solutions
        # Simplifies to a_1 * X_1 + a_2 * X_2 = P1
        # min 3*a_1 + a_2
        # s.t. a_1 * X_1 + a_2 * X_2 = P1
        a_1 = 0
        min_a_1 = 0
        min_a_2 = 0
        min_cost = math.inf
        while a_1 <= P_1:
            a_2 = (P_1 - a_1 * X_1) / X_2
            if a_2.is_integer(): # Valid solution
                if min_cost > 3 * a_1 + a_2 and a_1 * Y_1 + a_2 * Y_2 == P_2: # Need to check if a_1, a_2 satisfy the second equation as well
                    min_cost = 3 * a_1 + a_2
            a_1 += 1
        return min_cost

def main():
    game_num = 1
    with open("day13.txt", "r") as f:
        for l in f:
            if l == "\n":
               game_num += 1
            else:
                l = l.strip()
                if "+" in l:
                    pl_1 = l.index("+")
                    pl_2 = l.index("+", pl_1+1)
                    c_pos = l.index(",")

                    X_pos = l[pl_1+1:c_pos]
                    Y_pos = l[pl_2+1:len(l)]

                    if "A" in l: # Button A
                        A[game_num] = (int(X_pos), int(Y_pos))
                    else: #Button B
                        B[game_num] = (int(X_pos), int(Y_pos))
                else: # Prizes
                    eq_1 = l.index("=")
                    eq_2 = l.index("=", eq_1+1)
                    c_pos = l.index(",")

                    X_prize = l[eq_1+1:c_pos]
                    Y_prize = l[eq_2+1:len(l)]
                    prize[game_num] = (int(X_prize), int(Y_prize))
                    prize_[game_num] = (int(X_prize)+10000000000000, int(Y_prize)+10000000000000)
    tot_p1 = 0
    tot_p2 = 0
    for game in A:
        loc = solveGame_P1(game)
        loc_2 = solveGame_P2(game)
        if loc != "No Solution" and loc != math.inf:
            tot_p1 += loc
        if loc_2 != "No Solution" and loc != math.inf:
            tot_p2 += loc_2
    print(tot_p1) # Part 1: 29517
    print(tot_p2) # Part 2: 103570327981381
                
if __name__ == "__main__":
    main()