(ns layton-treepartion.core
  (:require [clojure.math.combinatorics :as combo])
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
   [1 [18 13]]     ;12
   [3 [9 12 14]]   ;13
   [0 [10 13 15]]  ;14
   [0 [11 14]]     ;15
   ]
  )





;(def puzzle [ [0 1 3 0] [2 1 2 1] [2 3 3 2] [1 3 0 0]])
;; up right down left
;; 0 move up, 1 move right, 2 move down, 3 move left
;(def walkmath [[0 -1] [1 0] [0 1] [-1 0]])
(def puzWidth 4)
(def puzHeight 4)

(defn getxy [puz position]
  (let [x (nth position 0)
        y (nth position 1)]
    (cond (> x 3) -1
          (< x 0) -1
          (> y 3) -1
          (< y 0) -1
          :default (nth  (nth puz y) x)))
  )

(defn valid [sol]
  ;#dbg
  (if (and
       (not (some #(= -1 %) sol))
       (= (count (distinct sol)) 4)
       ) true false )
  )


;; try every path we can and find all the solutions
;; you can make at this current xy pair
(defn allSolutions [path squares count x y solutions]
  ; #dbg
  (if (> count 3)
    ;; if we have reached the end of the road
    ;; check to see if the path is valid
    ;; if it is, append it to the solutions and return that
    ;; otherwise just return the solutions
    (if (valid path)
      [solutions (clojure.string/join "," squares)]
      nil
      )

    ;; if we can still move forward
    (concat
     (allSolutions (concat path [(getxy puzzle [x (dec y)])]) (concat squares [(+  x (* (dec y) puzWidth))]) (inc count) x (dec y) solutions)
     (allSolutions (concat path [(getxy puzzle [x (inc y)])]) (concat squares [(+  x (* (inc y) puzWidth))]) (inc count) x (inc y) solutions)
     (allSolutions (concat path [(getxy puzzle [(inc x) y])]) (concat squares [(+  (inc x) (* y puzWidth))]) (inc count) (inc x) y solutions)
     (allSolutions (concat path [(getxy puzzle [(dec x) y])]) (concat squares [(+  (dec x) (* y puzWidth))]) (inc count) (dec x) y solutions)
     )

    )
  )

;; simple wrapper to allSolutions to clean up the data
;; and return just unique values
(defn uniqueSolutions [x y]
  (filter #(not (empty? %)) (distinct (allSolutions [] []  0 x y [])))
  )



(defn -main
  [ & argc ]

  ;#dbg
  ; (uniqueSolutions 0 0)

  (def alls
    (combo/combinations
     (flatten
      (filter (fn [s] (not (empty? s)))
              (for [x (range 4) y (range 4)]
                (uniqueSolutions x y)
                )
              )) 4 )
  )

  (doall (filter #(= 16 (count (distinct (clojure.string/split (clojure.string/join  "," % ) #",")))) alls))
  )
