## Day 15 (AoC 2024)

## Part 1

Part 1 was implemented in two ways - a naive queue and a priority queue via min-heap via `heapq`. Min-heap drastically improves the queue in several ways:

* Early return if we are at the end of the mase (min-heap ensures that the first end instance is the smallest score)
* Large score paths are pushed to the end of the priority queue, so paths with smaller scores are popped and processed with higher frequency
* Visited nodes are represented as a dictionary mapping `(pos, d)` to score. But the visited check doesn't need a score check:
```
if (pos, d) in visited:
    continue
```
This is because min-heap ensures that the first `(pos, d)` processed must be associated with the smallest score with that configuration.

**Note:** `heapq.heappush` in this case uses tuple comparison to sift up and down, so `score` must be the first element in the tuple.

## Part 2

Part 2 was implemented by keeping track of the entire trail (as a set) in the tuple.

```
score, pos, d, _, trail = heapq.heappop(pq)
```
The `_` in the tuple the `epoch`, a monotonically increasing counter that increments every upsert into `heapq`. This is needed because of a corner case: if the node to be inserted and the node being compared have the same `score`, `pos`, `d`, then without `epoch` the `heapq` comparison falls back to trail. Set comparisons using `<` and `>` result in `TypeError`, so `epoch` is used to alway break the tie.

Another subtlety comes when inserting `trail` as a tuple element in the queue. `trail` is of type set, and thus
```
heapq.heappush(pq, (score+1000, (pos_x, pos_y), 'R', epoch, trail))
```
pushes a reference to the priority queue rather than creating a new copy. This is problematic because there may be diverging branches modifying the same set in memory. So, for every upsert, we need to create a copy of the trail before upsert.

### Focus Points
* Priority Queue via `heapq`
* Min-heap properties
* References of mutable types
* Representation of the `visited` state (here we used a `dict` rather than a `set` because not every move incremeents the player)