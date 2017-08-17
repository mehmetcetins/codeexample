;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname |str function|) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
; lang advanced student
(define a "mehmet")

(string-append a " çetin")

(string-length a)

(string-ith a 4)

(string-append a (number->string (string-length a)))

(or #true #false)
(and #true #false)

(define y  0)

(if (= y 0) 0 (+ y 1))