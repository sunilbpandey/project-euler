module P015.P015 (solution) where

fac :: Integer -> Integer
fac = foldr (*) 1 . enumFromTo 1

solution :: Integer
solution = div (fac 40) ((fac 20) * (fac 20))
