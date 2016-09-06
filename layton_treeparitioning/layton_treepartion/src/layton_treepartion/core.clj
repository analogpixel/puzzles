(ns layton-treepartion.core
  (:use clojure.set)
  (:require [clojure.math.combinatorics :as combo] )
  )


; type connections
; a=0 b=1 c=2 d=3
(def puzmap
  [
   [0 [1 4]]       ;0
   [1 [0 2 5]]     ;1
   [3 [1 3 6]]     ;2
   [0 [2 7]]       ;3
   [2 [0 5 8]]     ;4
   [1 [1 4 6 9]]   ;5
   [2 [2 5 7 10]]  ;6
   [1 [3 6 11]]    ;7
   [2 [4 9 12]]    ;8
   [3 [5 8 10 13]] ;9
   [3 [6 9 11 14]] ;10
   [2 [7 10 15]]   ;11
   [1 [8 13]]     ;12
   [3 [9 12 14]]   ;13
   [0 [10 13 15]]  ;14
   [0 [11 14]]     ;15
   ]
  )

;; return lists that have less than or equal to 4 items
;; in them
(defn lte4 [l]
  (filter #(<= (count %) 4) l)
  )

;; return lists that have less than 4 items
(defn lt4 [l]
  (filter  #(< (count %) 4) l)
  )

;; return lists that have 4 items in them
(defn eq4 [l]
  (filter  #(= (count %) 4) l)
  )

;; return all the moves that could be made from this square
;; then return only solutions with 4 or less
(defn validMoves [sq]
  (lt4 (map #(concat % #{sq} ) (combo/subsets (last(puzmap sq )) )))
  )

;; merge m2(item) onto every entry of m1(list)
(defn mergeCurrent [m1 m2]

  (loop [s (map vec (lte4 (map #(clojure.set/union (set m2) (set %))  m1))) solution []]

    ;; to remove duplicates keep the first item, and then filter out
    ;; any items that match that one in the list
    (if (empty? s)
      solution
      (recur
       (filter #(not= % (first s )) (rest s) )
       (conj solution (first s))
       )
      )

  )
  )

;; given 2 lists, keep all the items that have 4 items,
;; then merge m1 with m2 keeping all the items that have 4 and under
;; merge the first two lists with the last
(defn combinesq [m1 m2]

  (let [keep1 (eq4 m1)
        keep2 (eq4 m2)
        new (mapcat  #(mergeCurrent (lt4 m1) % ) (lt4 m2))
        ]
    (concat keep1 keep2 new)
    )
  )


;; walk the map until solutions can't hold anymore
;; by that I mean each list has 4 entries.
;; keep tract of moves so we don't walk over outselves
(defn walkmap [sq moves solution]
  (if (empty? (lt4 solution))
    solution
    (mapcat
     #(walkmap
       %
       (clojure.set/union moves #{%})
       (combinesq (validMoves %) solution)
       )
     (clojure.set/difference (set(last (puzmap sq))) moves  )
     )
    )
  )


; walkmap will return duplicate entries, so convert it to a set to
; a set to remove those duplicate entries
(defn getsquare [x]
  (set (walkmap x #{x} (validMoves x)))
  )

;; a valid list has 4 non duplicate entries in it.
(defn valid [l]
  (filter #(= 4 (count (distinct (mapcat (fn [x] (list (first (puzmap x)))) % ))))
          l)
  )

;; given a square, return the valid solutions for that square
(defn solutionsforsq [sq]
  (valid (getsquare sq))
  )

(defn -main
  [ & argc ]
  (def allmoves (mapcat #(solutionsforsq %) (range 16)))
  (println (filter #(= 16 (count (distinct (flatten %)))) (combo/combinations allmoves 4)))
  )


;; (([0 4 9 5] [1 6 3 2] [7 15 11 10] [13 12 14 8]))
