(define (inner_product v1 v2)
  (if (or (null? v1) (null? v2))
      0
      (+ (* (car v1) (car v2))
         (inner_product (cdr v1) (cdr v2)))))

(inner_product '(1 2 3) '(4 5 6))