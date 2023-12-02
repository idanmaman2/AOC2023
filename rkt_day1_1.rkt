#lang racket/base
(require racket/string)
(require racket/list)
(define (read-file-lines in)
  (define (parse-line line)
    (define (find-first-digit ln)
      (let ([first-char (car ln)])
        (cond
          [(empty? ln) (raise 'ValueError #t)]
          [(char-numeric? first-char)  (string first-char)]
          [else (find-first-digit (cdr ln))])))
    (define (find-last-digit ln)
      (let ([last-char (list-ref ln (- (length ln) 1))])
        (cond
          [(empty? ln) (raise 'ValueError #t)]
          [(char-numeric? last-char)  (string last-char)]
          [else (find-last-digit (drop-right ln 1))])))
    (string->number (string-append (find-first-digit (string->list line)) (find-last-digit (string->list line)))))
  (let ([line (read-line in)])
    (cond
      [(eof-object? line) 0]
      [else (+ (read-file-lines in) (parse-line line))])))
(let ([inp (open-input-file "./input.txt")]) (display (read-file-lines inp)))