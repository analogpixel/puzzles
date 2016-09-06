(ns layton-trashmoving.core)

; aa1111
; aa1111
; bbcc00
; bbcc11
; ddee11
; ffgg11
; 110011
; 110011


; up/down for every a, it must be able to move 6 or -6  for a valid move
; for every a, it must be able to move 2 or -2 and get 0
; if valid move found, recurse with the swap of the parts
; aa1111aa1111bbcc00bbcc11ddee11ffgg11110011110011

(def puz '(a a 1 1 1 1 a a 1 1 1 1 b b c c 0 0 b b c c 1 1 d d e e 1 1 f f g g 1 1 1 1 0 0 1 1 1 1 0 0 1 1) )

; (def validparts ['a 'b 'c 'd 'e 'f 'g])
(def validparts ['g 'f 'e 'd 'c 'b 'a])
;(def validparts ['g 'f ])

(defn pos [inlist item]
  ;#dbg
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


; from listin swap item n1 and n2
(defn swap [listin n1 n2]
  (loop [li listin
         c 0
         lo []
         itema (nth listin n1)
         itemb (nth listin n2)]
    (cond
      (empty? li) lo
      (= c n1) (recur (rest li) (inc c) (conj lo itemb) itema itemb)
      (= c n2) (recur (rest li) (inc c) (conj lo itema) itema itemb)
      :default (recur (rest li) (inc c) (conj lo (first li)) itema itemb)
    )
    )
  )

;; error moving 2 down and up at a time, instead of just one up and down at a time

;; (defn up ([blockcount] -6) ([] 'up ))
;; (defn down ([blockcount] 6) ([] 'down ))
;; (defn left ([blockcount] -2 ) ([] 'left ))
;; (defn right ([blockcount] 2 ) ([] 'right))
;; (def validmoves [up down left right])
;; (def reversemoves {'up down 'down up 'left right 'right left})

(def validmoves [-6 6 -2 2])

(defn move? [puzzle item direction]
  (let [
        poslist (pos puzzle item)
        poscount (count poslist)
        jmp (direction poscount)
        ]
    (try
      (= poscount (count
                   (filter
                    #(or
                      (= 0 (nth puzzle (+ % jmp)))
                      (= item (nth puzzle (+ % jmp)))
                      )
                    poslist)
                   )
         )

      (catch Exception e false)
      )
      )
    )

(defn move [puzzle item direction]
  (let [
        initialpos (pos puzzle item)
        poscount   (count initialpos)
        newpos     (map #(+ (direction poscount) %) initialpos)
        ]

    (loop [li puzzle
           pos1 initialpos
           pos2 newpos
           ]
      (if (empty? pos1)
        li
        (recur (swap li (first pos1) (first pos2)) (rest pos1) (rest pos2))
      )
    )
    )
  )

(defn solved? [puzzle]
  (= '( a a a a) (take-last 4 puzzle))
  )



(defn solve [puzzle lastp lastm count]
  ;#dbg
  (cond
    (solved? puzzle) true
    (> count 20) false

    :default
    (loop [p validparts]

      (if (empty? p)
      false

      (if
          (loop [m validmoves]
            (if (empty? m)
              false
              (if (and
                   (not (and (= lastp (first p)) (= lastm (first m)))) ;; don't repeat the last move we made
                   (move? puzzle (first p) (first m))
                   (solve (move puzzle (first p) (first m)) (first p) (reversemoves ((first m))) (inc count)))

                  (do (println (m), p) true)
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

(defn -main
  [& argc]
  (println 'h)
 )
