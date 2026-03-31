#lang racket

(define (possible-game? game cubes-config)
  (let* ((cube-counts (make-hash '()))
         (game-info (map (λ (subset)
                           (for-each (λ (cube)
                                       (hash-update! cube-counts cube add1 0))
                                     subset)
                           (list (length subset)))
                         (rest (string-split game "; ")))))
    (and (= (hash-ref cube-counts 'red 0) (cadr cubes-config))
         (= (hash-ref cube-counts 'green 0) (caddr cubes-config))
         (= (hash-ref cube-counts 'blue 0) (cadddr cubes-config))
         (apply = game-info (cdr cubes-config)))))

(define (sum-of-possible-games games cubes-config)
  (let ((possible-games
         (filter (λ (game)
                   (possible-game? game cubes-config))
                 games)))
    (apply + (map (λ (game)
                    (string->number (first (string-split game ":"))))
                  possible-games))))

(define input
  "Game 1: 1 green, 2 red, 6 blue; 4 red, 1 green, 3 blue; 7 blue, 5 green; 6 blue, 2 red, 1 green
   Game 2: 1 green, 17 red; 1 blue, 6 red, 7 green; 2 blue, 4 red, 7 green; 1 green, 6 red, 2 blue")

(define cubes-config '(12 13 14)) ; Set the desired cube configuration

(define games (string-split input "Game "))

(displayln (sum-of-possible-games games cubes-config))
