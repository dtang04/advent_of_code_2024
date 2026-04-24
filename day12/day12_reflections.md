## Day 12 (AoC 2024)

Part 1: Used BFS to calculate area and perimeter for each island. One thing to remember is that in order to prevent duplicates from entering the queue, the `visited` set should add the new element on **enqueue**, not **dequeue**.

### Focus points
* BFS
