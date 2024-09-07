module P003.P003 where

import Data.List (group)

import ProjectEuler.PrimeUtils (primes, sqrtFloor)

factorize :: Integer -> [(Integer, Int)]
factorize n =
    map (\l@(x:xs) -> (x, length l)) . group . factors n $ takeWhile (<= sqrtFloor n) primes
    where
        factors m [] = [m]
        factors m (p:ps)
            | p > m        = []
            | mod m p == 0 = p:factors (div m p) (p:ps)
            | otherwise    = factors m ps

solution' :: Int
solution' = fromIntegral . fst . last . factorize $ 600851475143

-- Alternative solution, without calculating primes or keeping a list of factors
largestFactor :: Integer -> Integer
largestFactor 1 = 1
largestFactor n
    | even n    = largestFactor (div n 2)
    | otherwise = max 2 $ largestFactor' n 3
    where
        largestFactor' m d
            | d*d > m      = m
            | mod m d == 0 = max d $ largestFactor' (div m d) d
            | otherwise    = largestFactor' m (d+2)

solution :: Integer
solution = largestFactor 600851475143
