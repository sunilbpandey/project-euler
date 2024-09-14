module P021.P021 (solution) where

import Data.List (nub, sort)
import ProjectEuler.PrimeUtils (sqrtFloor)

divisors :: Integer -> [Integer]
divisors n = (sort . concat) [nub [d, div n d] | d <- [1..(sqrtFloor n)], mod n d == 0]

properDivisorSum :: Integer -> Integer
properDivisorSum = sum . init . divisors

amicable :: Integer -> Bool
amicable n = let m = properDivisorSum n in m /= n && n == properDivisorSum m

solution :: Integer
solution = (toInteger . sum . filter amicable) [2..9999]
