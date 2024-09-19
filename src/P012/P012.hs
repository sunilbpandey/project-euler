module P012.P012 (solution) where

import Data.List (find)
import Data.Maybe (fromJust)

import ProjectEuler.PrimeUtils (factorize)

numDivisors :: Integer -> Int
numDivisors n = foldr ((*) . (+1) . snd) 1 (factorize n)

solution :: Integer
solution = (minimum . fromJust . find ((>0) . length)) [triangleNums k | k <- [1,2..]]
    where
        triangleNums k = map (*k) $ filter (test k) [2*k-1, 2*k+1]
        test k m = (numDivisors k) * (numDivisors m) > 500
