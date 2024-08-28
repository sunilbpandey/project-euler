module P001 where

solution :: Int
solution = sum [n | n <- [1..999], mod n 3 == 0 || mod n 5 == 0]
