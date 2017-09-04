;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname agirlikligraf) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
;kimden kime ağırlık
(define harita
  (list (list 1 2 1)
        (list 1 3 3)
        (list 2 3 2)
        (list 3 2 2)
        (list 2 7 1)
        (list 2 4 2)
        (list 3 5 3)
      )
  )


(define (alt alist n)(
                      if(empty? alist)
                        alist
                        (if (= n (first (first alist )))
                            (cons (rest (first alist)) (alt (rest alist) n))
                            (alt (rest alist) n )
                            )
                )
  )
(define (karsilastir alt1  alt2)(if(empty? alt2)
                                  alt1
                                (if(> (first (rest alt1)) (first (rest alt2)))
                                  alt2
                                  alt1
                                )))
(define (min-alt alist) (
                         if(empty? alist)
                           alist
                           (karsilastir (first alist) (min-alt (rest alist)))
                         ))

(define (ucs alist baslangic bitis) (
                                     if(empty? (alt alist baslangic))
                                       alist
                                       (if (= bitis (first (min-alt (alt alist baslangic))))
                                           1
                                           (
                                            (cons baslangic (min-alt (alt alist baslangic)))
                                            (ucs alist (first (min-alt (alt alist baslangic))) bitis)
                                           )
                                        )
                                     
                                     ) )

(ucs harita 1 87)