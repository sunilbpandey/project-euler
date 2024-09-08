module P009.P009 where

solution :: Integer
solution = head [2 * m * n * (m^4 - n^4) | m <- [1..21], n <- [1..(m-1)], m * (m + n) == 500]
