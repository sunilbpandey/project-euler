module P001.P001 where

solution :: Integer
solution = sum [n | n <- [1..999], mod n 3 == 0 || mod n 5 == 0]

main :: IO ()
main = print solution
