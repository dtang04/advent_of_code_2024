## Day 11 (AoC 2024)

The part 2 for this day utilized memoization. The key insight was that instead of storing the exact state of the list of stones, we could find the number of stones each stone would eventually create with $x$ blinks remaining, effectively turning the problem into a recursive subproblem. Another key insight was that the number of stones a stone would eventually create is independent of other stones, meaning that we could compute the recursive call on the beginning list of stones separately.

Since the arguments of the recursive subproblem are immutable (stone number, number of blinks remaining), memoization can be done via caching.

### Focus points
* Memoization
* Recursion

