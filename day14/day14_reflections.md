## Day 14 (AoC 2024)

## Part 1

This problem was a fairly standard simulation problem. One realization that did take some thought was the wrapping logic. Rather than try to calculate the index changes manually, it ended up being easy with modulo:

```
pos_x = (pos_x + dx) % board_length_x
pos_y = (pos_x + dy) % board_length_y
```

Storing the robots in a dict of `{(pos_x, pos_y) : [(d_x1, d_y1, (d_x2, d_y2)]}`, i.e. a dict whose keys were positions and values were lists of robots with different directions, made operations a bit slower, but the representation worked out and was intuitive.

## Part 2

This problem involved trying to find the easter egg (a Christmas tree) by simulating the robots' changes in direction for each unit of time. This problem is fairly open-ended, the approach I decided on was to count the number of consecutive robots that lined up in a particular row at a particular instance in time (which is a low-probability event if robots were randomly distributed). If this number exceeded a threshold of 10, then there is reasonable evidence that the simulation contains the easter egg.

### Focus Points
* Data structures
* Modulo operator
* Pattern detection