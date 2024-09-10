module ProjectEuler.PrimeUtils where

import Data.List (group)
import qualified Data.Map as Map

sqrtFloor :: Integer -> Integer
sqrtFloor = floor . sqrt . fromIntegral

isPrime :: Integral a => a -> [a] -> Bool
isPrime _ [] = True
isPrime n (p:ps) = mod n p /= 0 && isPrime n ps

sieve :: [Integer] -> [Integer]
sieve xs = sieve' xs Map.empty
    where
        sieve' [] _ = []
        sieve' (y:ys) m =
            case Map.lookup y m of
                Nothing      -> y:sieve' ys (Map.insert (y*y) [y] m)
                Just factors -> sieve' ys $ foldr advance (Map.delete y m) factors
            where
                advance p = Map.insertWith (++) (y+p) [p]

primesUpTo :: Integer -> [Integer]
primesUpTo n = sieve [2..n]

primes :: [Integer]
primes = sieve [2..]

primes' :: [Integer]
primes' = 2:[n|n <- [3,5..], isPrime n (takeWhile (<= sqrtFloor n) primes)]

factorize :: Integer -> [(Integer, Int)]
factorize n =
    map (\l@(x:xs) -> (x, length l)) . group . factors n $ takeWhile (<= sqrtFloor n) primes
    where
        factors m [] = [m]
        factors m (p:ps)
            | p > m        = []
            | mod m p == 0 = p:factors (div m p) (p:ps)
            | otherwise    = factors m ps
