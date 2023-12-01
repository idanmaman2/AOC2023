#lang racket/base
(require racket/string)
(require racket/list)

(define (read-file-lines in)
  (define (parse-line line)
    (define digits (hash 
            "one" 1 
            "two" 2
            "three" 3
            "four" 4
            "five" 5
            "six" 6
            "seven" 7 
            "eight" 8 
            "nine" 9
            "1" 1
            "2" 2 
            "3" 3
            "4" 4
            "5" 5
            "6" 6
            "7" 7
            "8" 8
            "9" 9
        ))
    (define (is-number-imp line func)
        (define (rec-is-number-imp dg)

                (cond 
                    [(empty? dg) (void)]
                    [(zero? (string-length line)) (void) ]
                    [(func line (car dg))
                     (hash-ref digits (car dg))
                    ]
                    [
                        else 
                        (rec-is-number-imp  (cdr dg ))
                    ]
                ) 
        )
        (rec-is-number-imp (hash-keys digits))
    )

    (define (find-first-digit ln)
      (let ([res (is-number-imp ln string-prefix? )])
        (cond
          [(empty? ln) (raise 'ValueError #t)]
          [(void? res) (find-first-digit (substring ln 1))]
          [else res])))

    (define (find-last-digit ln)
      (let ([res (is-number-imp ln string-suffix? )])
        (cond
          [(empty? ln) (raise 'ValueError #t)]
          [(void? res) (find-last-digit (substring ln 0 ( - (string-length ln) 1)))]
          [else res])))
  (+ (find-last-digit line) (* (find-first-digit  line) 10))
  
  
  )
  (let ([line (read-line in)])
    (cond
      [(eof-object? line) 0]
      [else (+ (read-file-lines in) (parse-line line))])))

(define inp (open-input-file "./input.txt"))
(display (read-file-lines inp))