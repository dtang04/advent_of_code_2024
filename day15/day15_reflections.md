## Day 15 (AoC 2024)

## Part 1

Part 1 was fairly standard. There was an optimization that I missed in the implementation regarding moving the boxes, if a gap exists:

When there is something like:
```
@OOOOOO.#

>
```

It's much easier to just move the front box to the empty spot and iterate the character `@` to the right, instead of shifting one by one. The implementation I used was if there was a box, keep iterating until we find a `.` or `#`. If `#`, then there is no valid move, if `.`, then backtrack, shifting all boxes one position in the intended direction.

## Part 2

Part 2 was much longer. The key issue is that while you can have a clean column such as this
```
@
[] 
[]

v
```
it's also possible to have the following configurations (only the `v` direction is shown for simplicity):
```
       @.      @         @
   1.  [] 2.   []  3.    []        
      [][]    []          []

v
```
The best way to go about this is use a recursive approach, exploring boxes deeper in the tree and checking if there are any walls. The moment there is a wall, none of the boxes can be moved.

While this seems intuitive, there were several things that made implementing somewhat tedious:
1. Have to store the boxes to be moved to prevent retraversal
2. Each box's representation was overly complicated in my implementation: I stored a box as `box = (box_l_x, box_l_y), (box_r_x, box_r_y))`
3. Have to consider all four directions (though `^` and `v` were similar, and so were `>` and `<`).

### Focus Points
* Recursion and dependency trees
* 2-D Lists
* Board representation
* Abstracting a large operation into smaller, individual cases