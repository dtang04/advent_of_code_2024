## Day 12 (AoC 2024)

Part 1: Used BFS to calculate area and perimeter for each island. One thing to remember is that in order to prevent duplicates from entering the queue, the `visited` set should add the new element on **enqueue**, not **dequeue**.

Part 2: The counting edge algorithm still uses BFS, but instead of just incrementing the perimeter, appends to a list of 3-tuples `(pos_x, pos_y, orientation)`. The realization is the following, and is the key logic behind `consolidateEdges`:

For `(pos_x, pos_y, "U")` (i.e. we hit the edge while going up) and `(pos_x, pos_y, "D")` (we hit the edge going down),
an edge is all 3-tuples that have `(pos_x, *, "U")` for the former and `(pos_x, *, "D")` for the latter. So to count edges, we just have to dedup all 3-tuples that share this configuration, given a `(pos_x, pos_y, "U")` or `(pos_x, pos_y, "D")`.

Similarly, for `(pos_x, pos_y, "R")`, `(pos_x, pos_y, "L")`, an edge is all 3-tuples that have `(*, pos_y, "R")` for the former and `(*, pos_y, "L")` for the latter. So, to count edges, we use the same deduping logic. 

### Focus points
* BFS
* Data structures (how to store information about a cell's contribution s.t. we can calculate an edge)

