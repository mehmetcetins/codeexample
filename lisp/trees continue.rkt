;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname |trees continue|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define tree (list 53
                   (list 23
                         (list 11 '() '())
                         (list 4 '() '())
                    )
                   (list 17 '() '())))

(define (node agac) (first agac))
(define (sol agac) (car (cdr  agac)))
(define (sag agac) (car (cdr (cdr  agac)))) 
(define (eb2 a b) (if (> a b ) a b))
(define (eb3 a b c) (eb2 (eb2 a b) (eb2 a c)))
(define (n tree) (if (empty? tree) 0 (eb3 (node tree) (n (sol tree)) (n (sag tree)))))
(n tree)