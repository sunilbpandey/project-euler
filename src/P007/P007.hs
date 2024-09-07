module P007.P007 where

sqrtFloor :: Integer -> Integer
sqrtFloor = floor . sqrt . fromIntegral

isPrime :: Integral a => a -> [a] -> Bool
isPrime _ [] = True
isPrime n (p:ps) = mod n p /= 0 && isPrime n ps

primes :: [Integer]
primes = 2:[n|n <- [3,5..], isPrime n (takeWhile (<= sqrtFloor n) primes)]

solution :: Integer
solution = primes !! 10000

main :: IO ()
main = print solution
