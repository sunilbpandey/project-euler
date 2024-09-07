module P005.P005 where

solution :: Integer
solution = foldl lcm' 1 [2..20]
    where
        gcd' a b = if b == 0 then a else gcd' b (mod a b)
        lcm' a b = div (a * b) (gcd' a b)

main :: IO ()
main = print solution
