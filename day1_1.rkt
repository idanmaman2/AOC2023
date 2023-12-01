; not finished or something . 
#lang racket/base
(define (read-file-lines in)
  (let ([line (read-line in) ])
    (cond
      [(eof-object? line) (list)]
      [else (append (list line) 
      
      (let ([line (read-file-lines in)]) 
        (string-)
      )
      
      
      )]
      
      
      )))

(define inp (open-input-file "./input.txt"))
(display (read-file-lines inp) ) 
