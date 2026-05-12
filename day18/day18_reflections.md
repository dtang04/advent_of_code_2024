## Day 18 (AoC 2024)

## Part 1

This was a standard BFS problem. We don't need `heapq` because the visited set stores positions uniquely.

## Part 2

My solution wasn't the most efficient, I used a brute force solution where I ran BFS for every additional tile dropped, but it was able to pass the test because BFS itself is fairly efficient for a 70 x 70 grid.

A better way would be to use binary search to try to find the first instance in which the path is blocked. This is because after the path is blocked, it can no longer be reopened.

### Focus Points
* BFS
* Grid representation


