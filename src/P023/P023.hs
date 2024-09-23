module P023.P023 where

import qualified Data.Set as S

import ProjectEuler.Common (properDivisorSum)

abundant :: Integer -> Bool
abundant n = properDivisorSum n > n

abundants :: [Integer]
abundants = filter abundant [1..28123]

abundants' :: S.Set Integer
abundants' = S.fromList abundants

abundant' :: Integer -> Bool
abundant' = flip S.member abundants'

isAbundantSum :: Integer -> Bool
isAbundantSum n = any abundant' [n - x | x <- takeWhile (<= (div n 2)) abundants]

solution :: Integer
solution = toInteger $ sum $ filter (not . isAbundantSum) [1..28123]
