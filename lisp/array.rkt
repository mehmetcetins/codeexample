;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname array) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(list 1 2 3 "a" "b" 3)

(define a (list 1 2 3))
a
(first a)
(car a)
(rest a)
(cdr a)
(append (list 10) a )

a

(cons 10 a)
(cons (list 10) a)

(define (bindir f b) (
                if (empty? b) b
                   (cons (f (car b)) (bindir f (rest b)))
               )
              )
(define (yenif a) ( * a a))
(bindir yenif a)