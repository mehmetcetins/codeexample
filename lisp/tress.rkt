;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname tress) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define tree (list 1
                   (list 2 '() '())
                   (list 3 '() '())
                   ))




(define (topla tree)
  (if  (empty? tree) 0
     (+ (first tree)  (topla (first (rest tree)))
        (topla (first (rest (rest tree))))))
  )

(topla tree)