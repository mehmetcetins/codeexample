;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname |if statement|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define a 10)
(define b 15)
(if
  (= a b)
  (print "eşit")
  (if
     (> a b)
     (print "a büyük ")
     (print "b büyük")
     
     )
)


(cond [(= a b) (print "eşit")]
      [(> a b) (print "a büyük")]
      [(< a b) (print "b büyük")]
      )