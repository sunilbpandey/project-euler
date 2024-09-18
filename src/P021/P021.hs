module P021.P021 (solution) where

import ProjectEuler.Common (properDivisorSum)

amicable :: Integer -> Bool
amicable n = let m = properDivisorSum n in m /= n && n == properDivisorSum m

solution :: Integer
solution = (toInteger . sum . filter amicable) [2..9999]
