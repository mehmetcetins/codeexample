;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname tictactoe) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define tahta (list (list 1 0 1) (list 0 -1 0) (list -1 0 1) ))


(define (satirKontrol satir)
  (if (= (first satir) (second satir) (third satir))
      (first satir)
      0
      )
  )


(define (artir sayi)(+ 1 sayi))

(map satirKontrol tahta)
(define (eksen tahta)(list (list (first (first tahta)) (second (second tahta)) (third (third tahta)))
                           (list (third (first tahta)) (second (second tahta)) (first (third tahta)))
                           ))
(define (dondur tahta) (list (map first tahta)
                             (map second tahta)
                             (map third tahta)
                             ))
(define (eksenKontrol liste)(if (= (first liste ) (second liste))
                                (first liste)
                                0
                                )
  )
(dondur tahta)
(eksen tahta)
(eksenKontrol (first tahta))