module ProjectEuler.Common where

import Data.Char (digitToInt)

digitSum :: Show a => a -> Integer
digitSum = toInteger . sum . (map digitToInt) . show

fac :: Integer -> Integer
fac = product . enumFromTo 1
