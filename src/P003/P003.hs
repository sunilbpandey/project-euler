module P003.P003 where

import ProjectEuler.PrimeUtils (factorize)

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
