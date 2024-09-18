module ProjectEuler.Common where

import Data.Char (digitToInt)
import Data.List (nub, sort)

import ProjectEuler.PrimeUtils (sqrtFloor)

digitSum :: Show a => a -> Integer
digitSum = toInteger . sum . (map digitToInt) . show

fac :: Integer -> Integer
fac = product . enumFromTo 1

divisors :: Integer -> [Integer]
divisors n = (sort . concat) [nub [d, div n d] | d <- [1..(sqrtFloor n)], mod n d == 0]

properDivisorSum :: Integer -> Integer
properDivisorSum = sum . init . divisors
