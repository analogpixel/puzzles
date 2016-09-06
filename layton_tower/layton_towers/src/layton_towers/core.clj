(ns layton-towers.core)

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



(defn -main
  [ & args]

  (println "starting")
  (def startList [[1 2 3 100] [100] [100]] )
  (solve (validSolutions startList) 0)
  (println "ending")

  )
