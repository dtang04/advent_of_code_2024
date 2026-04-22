## Day 10 (AoC 2024)

This day was fairly straightforward, with the hardest part understanding how to get the counting trailhead logic correct in part 1. I ended up deciding on a dictionary with the start tuple as a key mapping to a list of end positions.

Then, I used BFS such that when the queue processed an entry with `level = 9`, if the start did not exist or the end position did not exist in the list that the start mapped to, it was added to the count and the corresponding end was appended onto the designated list. Otherwise, don't increment the counter and continue.

In part 2, BFS fit nicely into counting all unique paths to determine the rating.

### Focus points
* BFS
* Counting unique paths with BFS, counting what constitutes as a path correctl

