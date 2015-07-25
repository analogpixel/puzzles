#lang slideshow

; http://docs.racket-lang.org/reference/generic-numbers.html#%28part._.Bitwise_.Operations%29

(define box  #b111000000000111000000000111000000000111000000000111000000000111000000000111111111111111111111111 ) ; box starts out empty

(define shapes '(
                 #b111000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 ;; 3  a
                 #b010000000000110000000000010000000000000000000000000000000000000000000000000000000000000000000000 ;; -| b
                 #b111000000000111000000000111000000000000000000000000000000000000000000000000000000000000000000000 ;;3x3x3 c
                 #b111000000000011000000000011000000000011000000000000000000000000000000000000000000000000000000000 ;; 3x2x2x2 d
                 #b111000000000100000000000100000000000000000000000000000000000000000000000000000000000000000000000 ;; 3x1x1 e
                 #b111000000000111110000000111000000000000000000000000000000000000000000000000000000000000000000000 ;; 3x5x3 f
                 #b110000000000110000000000110000000000000000000000000000000000000000000000000000000000000000000000 ;; 2x2x2 g
                 #b111100000000011100000000000000000000000000000000000000000000000000000000000000000000000000000000 ));; 4x3 h
  



(define (drawBox  box)
  (for ([i (range 7 -1 -1)])
  (fprintf (current-output-port) "~b\n"
   (bitwise-and 
    (arithmetic-shift box (* -12 i))
     (- (expt 2 12) 1)
   )
  )
  )
  
)

; shift -1 moves right 01 becomes 00
; shift  1 moves left 01 becomes 010
(define (solve currentBox currentShapes offset)

 
  ;; (fprintf (current-output-port) "offset ~s currentBox: ~b \n" offset currentBox )

  ;; if the list is empty return the offset and end recusion 
  (if (empty? currentShapes)

      ;; true; list empty; return answer list
      #t
       
      ;; false ; figure out where this shape can go
      
      ;; if the previous current offset of the shape anded with 1 is 1, then we past the edge
      ;; of the shape and will start loosing parts of it so stop
  
      (if (= (bitwise-and 1 (arithmetic-shift (first currentShapes) (- offset 1) )) 0)

        
        (if
           ;; and the current shape with the current box, 0 means that no 1s overlap, so
           ;; this part can fit here
           ;; and if we get a true back from solve it has made it all the way to a solution
           (and 
           (= (bitwise-and currentBox (arithmetic-shift (first currentShapes) offset)) 0)
           ( solve
             (bitwise-ior currentBox (arithmetic-shift (first currentShapes) offset))
             (rest currentShapes)
              0 )
           )
         
           ;; good solution
           (begin
           (drawBox (bitwise-ior currentBox (arithmetic-shift (first currentShapes) offset)))
           (fprintf (current-output-port) "offset ~s \tpart: ~s  \tbox: ~b\n" offset (- (length shapes) (length currentShapes )) (bitwise-ior currentBox (arithmetic-shift (first currentShapes) offset)) )
           )
           
           ;; if we get a false back from solve then a higher solution has failed
           ;; and we need to try something else
           (solve currentBox currentShapes (- offset 1))

           ) ;; end if

        ;; the shape have moved to far, this is not valid
        #f
              ) ;; end if offset check

              
          ) ;; end check empty
) ;; end solve function



  ;;(drawBox box)
(solve box shapes 0 )
;;(fprintf (current-output-port) "offset  \tpart:   \tbox: ~b\n"  box )