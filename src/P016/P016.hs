module P016.P016 (solution) where

import Data.Char (digitToInt)

pow :: Integral a => a -> Int -> Integer
pow x y = toInteger $ foldr (*) 1 (replicate y x)

digitSum :: Show a => a -> Integer
digitSum = toInteger . sum . (map digitToInt) . show

solution :: Integer
solution = digitSum $ pow 2 1000
