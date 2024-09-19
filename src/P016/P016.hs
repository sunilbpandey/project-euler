module P016.P016 (solution) where

import ProjectEuler.Common (digitSum)

pow :: Integral a => a -> Int -> Integer
pow x y = toInteger $ foldr (*) 1 (replicate y x)

solution :: Integer
solution = digitSum $ pow (2 :: Integer) 1000
