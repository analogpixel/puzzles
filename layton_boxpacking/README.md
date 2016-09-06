For this Doctor Layton Puzzle, you must pack objects into a suitcase, so a box packing algorithm of some sort.  Luckily you can't rotate any of the objects which makes this much easier.

I solved this in lisp (racket) using just binary.  To do this, I took an empty box:

```
000000000000
000000000000
000000000000
000000000000
000000000000
000000000000
```

and then I flattened it to one line

```
000000000000000000000000000000000000000000000000000000000000000000000000
```
Since I wanted to keep this all in happy multiples of 4bits, and the actual size of the box in question was not a multiple of 4bits, I added extra padding bits and just set them to 1, which means filled in.

```
111000000000111000000000111000000000111000000000111000000000111000000000111111111111111111111111
```

I then did this for each shape making each shape take up the same amount of bits as the box.

```
the bar shaped thing
111000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
```

With all of this, I was able to bitshift the parts to the right over and over to see if it fit in the box just by calling a bitwise and making sure it comes out 0 (no overlapping 1's).  I did this over and over recursively until I found a solution to the problem.

