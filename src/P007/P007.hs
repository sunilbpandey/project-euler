module P007.P007 where

import ProjectEuler.PrimeUtils (primes, sqrtFloor)

solution :: Integer
solution = primes !! 10000

main :: IO ()
main = print solution
