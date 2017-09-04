;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname fol) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(require racklog)

(%which () %true)
(%which () %fail)

(define %knows
  (%rel ()
        [('Odysseus 'TeX)]
        [('Odysseus 'Racket)]
        [('Odysseus 'Prolog)]
        [('Odysseus 'Penelope)]
        [('Penelope 'TeX)]
        [('Penelope 'Prolog)]
        [('Penelope 'Odysseus)]
        [('Telemachus 'TeX)]
        [('Telemachus 'calculus)]

   )

  )

(%which () (%knows 'Odysseus 'TeX))
(%which (what) (%knows 'Odysseus what))



(define %computer-literate
  (%rel (person)
        [(person) (%knows person 'TeX)
                  (%knows person 'Racket)
                  ]
        [(person) (%knows person 'TeX) (%knows person ' Prolog)]

        ))

(%which () (%computer-literate 'Penelope))

(%assert! %knows () [('Odysseus 'archery)])
(%which (who) (%knows who 'archery) )