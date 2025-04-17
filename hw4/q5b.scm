(define (interleave x y)
  (cond
    ((null? x) y)
    ((null? y) x)
    (else
     (cons (car x) (cons (car y) (interleave (cdr x) (cdr y)))))))

(interleave '(1 2 3) '(a b c))
(interleave '(1 2 3) '(a b c d e f))
(interleave '(1 2 3 4 5 6) '(a b c))