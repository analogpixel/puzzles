(ns longpath.core
  (require clojure.core)
  )

(def maxScore (atom 0))
(def maxList  (atom (list)))

(def w
  (hash-map
   :a '( (:b 1) (:e 1)),
   :b '( (:c 2) (:f 1) (:a 1)),
   :c '( (:d 1) (:h 1) (:b 2)),
   :d '( (:c 1) (:i 1)),
   :e '( (:a 1) (:f 1) (:m 1)),
   :f '( (:g 1) (:b 1) (:e 1)),
   :g '( (:f 1) (:h 1) (:o 2)),
   :h '( (:g 1) (:i 1) (:c 1)),
   :i '( (:d 1) (:h 1) (:j 1)),
   :j '( (:i 1) (:k 1) (:q 2)),
   :k '( (:j 1) (:n 1)),
   :l '( (:p 1) (:m 1)),
   :m '( (:t 2) (:l 1) (:e 1)),
   :n '( (:k 1) (:o 1) (:r 1)),
   :o '( (:n 1) (:g 2) (:p 1)),
   :p '( (:l 1) (:o 1) (:s 1)),
   :q '( (:finish 0)),
   :r '( (:q 1) (:n 1) (:s 2)),
   :s '( (:r 2) (:p 1) (:t 1)),
   :t '( (:s 1) (:m 2))
   )
  )


(defn solve [head solution score]

  (if (= (first (first head)) :finish)

    (if (> score @maxScore)
      (do (reset! maxScore score)
          (reset! maxList solution)

          )
      false
      )

    (let
        [ valid (filter #(not (.contains solution (first %) ) ) head ) ]
      (doall (map #(solve (w (first %)) (conj solution (first %)) (+ score (fnext %))) valid))
      )
    )


  )


(defn -main [&]
  (solve (w :a) (list :a) 0)
  (println (list @maxScore @maxList))
  )


