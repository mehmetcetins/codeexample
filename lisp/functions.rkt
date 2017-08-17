;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname functions) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define (a b)(* 2 b))
(a 500)

(define (sum a b)( + a b ))

(sum 1 6)

(define (uygula fonksiyon a b )(fonksiyon a b))

(uygula * 10 20)


(define (fak a)(if (= a 0) 1
                    (* a (fak (- a 1)))))
(fak 4)


(define (fibo n) 
                  (if (= n 1) 1
                      (if (= n 2) 1
                          (+ (fibo (- n 1) )
                             (fibo (- n 2))))))
(fibo 8)