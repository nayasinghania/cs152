(define (elements list)
 (cond
   ((null? list) 0)
   ((pair? list)
    (+ (elements (car list)) (elements (cdr list))))
   (else 1)))

(elements '(1 (2 (3) 4) 5 6))