module P004.P004 (solution) where

solution :: Integer
solution = maximum [x | x <- candidates, d <- [949,951..999], mod x d == 0, is3digit $ div x d]
    where
        candidates = [900009 + 10010*b + 1100*c | b <- [0..9], c <- [0..9]]
        is3digit n = 99 < n && n < 1000
