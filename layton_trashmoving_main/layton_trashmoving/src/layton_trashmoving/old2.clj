(ns layton-trashmoving.core
  (:require [clj-http.client :as client] [clojure.data.json :as json] [clojure.math.combinatorics :as combo])
  )


;; next step
;; fill in a solution and (reduce it to a puz
;; [(a 7) (a 7)...]

; (require '[clj-http.client :as client])

;; (def puz '(a a 1 1 1 1 1
;;            a a 1 1 1 1 1
;;            b b c c 0 0 1
;;            b b c c 1 1 1
;;            d d e e 1 1 1
;;            f f g g 1 1 1
;;            1 1 0 0 1 1 1
;;            1 1 0 0 1 1 1) )


;; moves we can make
;; ddd dd uu ul rd uuu ru dr ud uur luu lu uul u d l r

(def puz '(a a 1 1 1 1 1
           a a 1 1 1 1 1
           b b c c 0 0 1
           b b c c 1 1 1
           d d e e 1 1 1
           f f g g 1 1 1
           1 1 0 0 1 1 1
           1 1 0 0 1 1 1) )

(def puza '(a a 1 1 1 1 1
            a a 1 1 1 1 1
            b b c c 0 0 1
            b b c c 1 1 1
            d d e e 1 1 1
            0 0 0 0 1 1 1
            1 1 f f 1 1 1
            1 1 g g 1 1 1) )



(def puzb '(a a 1 1 1 1 1
            a a 1 1 1 1 1
            b b c c 0 0 1
            b b c c 1 1 1
            d d 0 0 1 1 1
            f f 0 0 1 1 1
            1 1 e e 1 1 1
            1 1 g g 1 1 1) )


;; given a, find out if the you add the movement you get all 0's or a's
;; (def ppuz [ [a (0 1 7 8)]
;;             [b (14 15 21 22) ]
;;             [0 (x y z v c)]
;;             ]

(def validparts ['a 'b 'c 'd 'e 'f 'g ])
(def validmoves [2 -2 7 -7 ])
(def allmoves (combo/cartesian-product validparts validmoves))

(def testmoves [(list 'g 7)])
(defn movetoend [l i]
  (conj (vec (remove #(= % i) l)) i)
  )

(defn movealltoend [l i]
  (concat (remove #(= (first %) i) l) (remove #(not= (first %) i) l) )

  )


(defn pos [inlist item]
  (loop [l inlist count 0 solution [] ]
    (if (empty? l)
      solution
      (if (= item (first l))
        (recur (rest l) (inc count) (conj solution count))
        (recur (rest l) (inc count) solution)
        )
      )

    )
  )

(defn upd-vec [input-vector ids new-values]
  (apply assoc input-vector (interleave ids new-values)))


(defn makemove [puzzle part direction]
  ; #dbg
  (let [
        p1 (pos puzzle part)
        p2 (map #(+ direction %) p1)
        ]
    (upd-vec (upd-vec (vec puzzle) p1 [0 0 0 0]) p2 [part part part part] )
             )
  )

(defn move? [puzzle item direction]
  ; #dbg
  (let [
        poslist (pos puzzle item)
        poscount (count poslist)
        ]
    (try
      (= poscount (count
                   (filter
                    #(or
                      (= 0 (nth puzzle (+ % direction)))
                      (= item (nth puzzle (+ % direction)))
                      )
                    poslist)
                   )
         )

      (catch Exception e false)
      )
      )
    )


;; only need to check one square assuming all moves are valid
(defn solved? [puzzle]

  (= 'a (nth puzzle 44))
  )


(defn sendpuz [puz]
   ; https://github.com/dakrone/clj-http/
  (client/get (str  "http://localhost:8080/data/?data=" (json/write-str  puz)) )
  )


(defn longrun? [l currentrun currentitem]
  (cond
    (empty? l) false
    ;(symbol? (first l)) false
    (= (first (first l)) 'a) false
    (= currentrun 3) true
    (= currentitem (first (first l))) (longrun? (rest l) (inc currentrun) currentitem)
    :default (longrun? (rest l) 1 (first (first l)))
    )
  )

(defn flipflop? [l lastitem lastmove]
  (cond
    ;(symbol? (first l)) false
    (empty? l) false
    (and (= lastitem (first (first l))) (= lastmove (* -1 (last (first l))))) true
    :default (flipflop? (rest l) (first (first l)) (last (first l)))
    )
  )



(defn toomany [l]


  (let [ mycounts
        (loop [counts {'a 0 'b 0 'c 0 'd 0 'e 0 'f 0 'g 0}
               parselist (flatten l)]
          (cond
            (empty? parselist) counts
            (symbol? (first parselist)) (recur (assoc counts (first parselist) (inc (counts (first parselist)))) (rest parselist))
            :default (recur counts (rest parselist))
            )
          )
        ]

    (cond
      (> (mycounts 'a) 15) true
      (> (mycounts 'b) 11 ) true
      (> (mycounts 'c) 10 ) true
      (> (mycounts 'd) 8) true
      (> (mycounts 'e) 3) true
      (> (mycounts 'f) 12) true
      (> (mycounts 'g) 5) true
      :default false
      )

    )
  )



(defn bad [puzzle l sc]
  (or
   (> sc 64)
   (and (> sc 12) (not= 'e (nth puzzle 19)))
   (flipflop? l nil nil)
   (longrun? l 0 nil)
   (toomany l)
   )
  )

(defn solvea [puzzle solution sc]
                                        ;
  ;#dbg
  ;(println solution)

  ; (when (> sc 60) (if (< 20000 (rand 20001)) (do (println solution) (sendpuz puzzle))))
  ;#dbg

  (if (solved? puzzle)
    (do  (println solution) true)
    (if (bad puzzle solution sc)
      false
      (some true?
            (map
             (fn [x] (solvea (makemove puzzle (first x) (last x)) (conj solution x) (inc sc)))
             (filter #(move? puzzle (first %) (last %)) allmoves)
             )
            )
      )
    )
  )

(defn ransolve [puz moves]

  (loop  [p puz
          m '(g 7)
          solution [] ]
    (if (< 20000 (rand 20001)) (sendpuz puz))

    (if (solved? p)
      solution
      (recur (makemove puz (first m) (last m))
             (rand-nth (filter #(move? puz (first %) (last %)) moves))
             (conj solution moves))
      )
    )
  )

(defn solve [puzzle moves count]

  ;#dbg
  ;(sendpuz puzzle)

  ;#dbg
  (if (solved? puzzle)
    true
    (if (or (> count 64) (empty? moves))
      false
      (if (if (move? puzzle (first (first moves)) (last (first moves)) )
            (solve (makemove puzzle (first (first moves)) (last (first moves)))
                   (movealltoend allmoves (first (first moves)))
                   (inc count))
            false
           )
        (do (println (first moves)) true)
        (recur  puzzle (rest moves) count)
        )
      )
    )
  )

(defn solveold [puzzle lastp lastm count]

  ;#dbg
  ;(sendpuz puzzle)

  (cond
    (solved? puzzle) true
    ;(> count 29) (do #dbg (sendpuz puzzle) false)
    (> count 29) false

    :default
;    (loop [p validparts]
    (loop [p (shuffle validparts)]

      (if (empty? p)
      false

      (if
          ; (loop [m validmoves]
          (loop [m (shuffle validmoves)]
            (if (empty? m)
              false
              (if (and
                   (not (and (= lastp (first p)) (= lastm (first m)))) ;; don't repeat the last move we made
                   (move? puzzle (first p) (first m))
                   (solve (makemove puzzle (first p) (first m)) (first p) (* -1  (first m)) (inc count))
                   )

                ;; true
                (do (println m, p) true)

                ;; false
                (recur (rest m))
                )
              )
            )

        ;; true
        true

        ;; false
        (recur (rest p))
        )
      )
      )
    )
  )


(def solution ['(g 7) '(g 7) '(f 2) '(f 7) '(d 7) '(d 2) '(b 7) '(b 7)
               '(c -2) '(e -7) '(e -7) '(e 2) '(d -7) '(d -7) '(d -7)
               '(b 2) '(b -7) '(f -7) '(f -2) '(b 7) '(b 7)
               '(c 7) '(c 2) '(a 7) '(a 7) '(a 7) '(d -2) '(d -7) '(d -7)
               '(a -7) '(a -7) '(f -7) '(f -7) '(c -7) '(b -7) '(b -2)
               '(c 7) '(c 7) '(c 7) '(f 2) '(f 7) '(a 7) '(a 2)
               '(b -7) '(b -7) '(b -7) '(f -2) '(f -7) '(c -7) '(c -2) '(a 7) '(a 7) '(a 7)
              '(f 2) '(f -7)  '(c -7) '(a -7) '(a -7) '(g -7) '(g -7) '(g -2) '(a 7) '(a 7) '(a 7)
              ])

(defn applypuz [p, s]
  ;#dbg
  (if (empty? s) p
      (if (move? p (first (first s)) (last (first s)))
        (do (println (first s)) (recur (makemove p (first (first s)) (last (first s))) (rest s)))
        (do (println "bad" (first s)) false)
        )
      )
  )

;; green b
;; red a
;; blue c
;; orange d
;; purple e
;; dark brown f
;; light brown g

(defn -main
  [& argc]
  (solvea puza ['(g 7) '(g 7) '(f 2) '(f 7)] 4)
 )
