module P003 where

import Data.List (group)

sqrtFloor :: Integer -> Integer
sqrtFloor = floor . sqrt . fromIntegral

isPrime :: Integral a => a -> [a] -> Bool
isPrime _ [] = True
isPrime n (p:ps) = mod n p /= 0 && isPrime n ps

primes :: [Integer]
primes = 2:[n|n <- [3,5..], isPrime n (takeWhile (<= sqrtFloor n) primes)]

factorize :: Integer -> [(Integer, Int)]
factorize n =
    map (\l@(x:xs) -> (x, length l)) . group . factors n $ takeWhile (<= sqrtFloor n) primes
    where
        factors m [] = [m]
        factors m (p:ps)
            | p > m        = []
            | mod m p == 0 = p:factors (div m p) (p:ps)
            | otherwise    = factors m ps

solution :: Int
solution = fromIntegral . fst . last . factorize $ 600851475143

main :: IO ()
main = print solution
