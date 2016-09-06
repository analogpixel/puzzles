(ns layton-trashmoving2.core
  (:gen-class))

;; for each slot: the item that is in that slot, and a list of
;; connections to other slots from there

; Holding, Up, Down, Left, Right
; 0=0 a=1 b=2 c=3 d=4 e=5 f=6 g=7
(def connections [
                  [1 false 1 false false ] ; 0 a is in loction and loc 1 is down
                  [1 0 2 false false]      ; 1 a is in location and 1 is up 2 is down
                  [2 1 5 false 3]          ; 2
                  [3 false 6 2 4]          ; 3
                  [0 false false 3 false]  ; 4
                  [2 2 7 false 6]          ; 5
                  [3 3 8 5 false]          ; 6
                  [4 5 9 false 8]          ; 7
                  [5 6 10 7 false]         ; 8
                  [6 7 false false 10]     ; 9
                  [7 8 11 9 false]         ; 10
                  [0 10 12 false false]    ; 11
                  [0 11 false false false] ; 12
                  ])

;; list of slots currently set to 0 (empty)
(def zeros [4 11 12])

(defn -main
  "I don't do a whole lot ... yet."
  [& args]
  (println "Hello, World!"))
