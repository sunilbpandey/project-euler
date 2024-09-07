module P006.P006 where

solution :: Integer
solution = 2 * sum [x*y | x <- [1..100], y <- [(x+1)..100]]
