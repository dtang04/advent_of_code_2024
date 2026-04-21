## Day 9 (AoC 2024)

Most of the time was spent on debugging part 2 of AoC day 9, as there were several corner cases that needed to be considered.

The biggest insight that took me some time to realize was that even though one file could not fit in an earlier space in the file system, we cannot just increment a global pointer to point to the next empty space. It is possible that a future file could fit into the space.

To see this, consider the following filesystem:

```
....AAA....BBBBB
```

BBBBB cannot fit into the gap at the beginning of the filesystem, but we cannot increment the pointer to the next empty space at index pos 7. Indeed, AAA can go in that gap, so the correctly organized filesyste is:

```
AAA........BBBBB
```

This means that for each subsequent file (assuming we read from right to left) must consider every possible empty space until the (pointer >= the beginning of the filesystem).

### A faster algorithm

A faster algorithm for part 2 would be:

Store each file as (start, length, id)
Store each free span as (start, length)

Then, for each file in descending ID:
* Scan the gap list from left to right
* Then, find the first gap with
    - gap.start < file.start and gap.length >= file.length
* Then, move the file by updating spans, shrinking or removing the processed gap
* Add a new gap where the file used to be

### Focus points
* Off-by-one indexing errors
* Thinking about the problem as an interval tracking problem can make the problem easier to think about



