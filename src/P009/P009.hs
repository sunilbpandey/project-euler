module P009.P009 (solution) where

pow :: Integer -> Integer -> Integer
pow x y = x^y

solution :: Integer
solution = head [(2 :: Integer) * m * n * ((pow m 4) - (pow n 4)) | m <- [1..21], n <- [1..(m-1)], m * (m + n) == 500]
