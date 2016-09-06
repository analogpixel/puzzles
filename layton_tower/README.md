This was one of those joys of programming where you know exactly what you want to do, but just can't seem to figure out how to make lisp do it.

All I wanted to do was take the current tower configuration, figure out all the different valid configurations, and then repeat that process over and over until I found the solution.  Now that I have a working solution it seems easy, but an easy that took me a few days to figure out.

One of the first problems I ran into, was how to move a value in a nested list within lisp.  My data structure for the towers was just a vector containing 3 vectors; each specifying one of the poles in the puzzle.  When a valid move is found, I needed to move a number from one list to another so I could pass that up the recusion chain to look for the next step:

```lisp
;; move the item at the top of l1 to the top of l2
(defn move [inlist l1 l2]
  (vec
   (for [i (range (count inlist))]
     (cond
       (= i l1) (vec (rest (inlist l1)))
       (= i l2) (vec (concat (list (first (inlist l1))) (inlist l2)))
       :else (inlist i)
       )
     ))
  )
```

But I guess that part of the code was ahead of itself.  First I needed to figure out what valid moves I could make with the current configuration:

```lisp
;; given 3 pillars, find all the valid moves we can make and
;; return a list of lists(pillars)
(defn validSolutions [indata]
  (vec
   (filter some?
           (for [x (range (count indata)) y (range (count indata))]
             (if (< (first (indata x)) (first (indata y)) )
               (move indata x y)
               nil
               )
             )
           ))
  )
```

When I started this endeavor, I was hoping that I could solve the entire puzzle in one line of maps filters and dodads, but it didn't turn out that way.

To solve the puzzle, I took a configuration, figured out all the valid moves, and then iterated through them all; stopping when I got to the known max solution.

```lisp
(defn solve [indata score]

  ;; if the score is greater than 7 or the list is empty then
  ;; this is not the correct solution so return false
  (if (or (> score 6) (empty? indata))
    false

    ;; head will get the first item to try
    ;; tail is everything else that will be tried later
    ;; solved is a boolean of if we have solved the puzzle
    (let [head (peek indata)
          tail (pop indata)
          solved (= (last head) [1 2 3 100])
          ]

      ;; if we have solved the puzzle then print the head and return true
      (if solved
        (do  (println head) true)

        ;; call solve with all the new possible solutions for the current head
        ;; if it comes back true, then somewhere upstream we have solved the puzzle
        ;; so print out the solution here and return true
        (if (solve (validSolutions head) (inc score))
          (do  (println head) true)

          ;; if false came back, then we need to try a different child branch
          (recur tail score)
          )
        )
      )
    )
  )
```
