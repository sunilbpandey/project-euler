module P002.P002 where

-- Fibonacci series implemented as an infinite list
fibonacci :: [Integer]
fibonacci = 1:1:zipWith (+) fibonacci (tail fibonacci)

-- Sum every even number less than 4000000
solution' :: Integer
solution' = sum . takeWhile (< 4000000) . filter even . tail $ fibonacci

every :: Int -> [a] -> [a]
every n xs = case drop (n-1) xs of [] -> []
                                   (y:ys) -> y:every n ys

-- Sum every third number less than 4000000
solution'' :: Integer
solution'' = sum . takeWhile (< 4000000) . every 3 $ fibonacci

takeUntil :: (a -> Bool) -> [a] -> [a]
takeUntil _ [] = []
takeUntil f (x:xs) = if f x then [x] else x:takeUntil f xs

lastN :: Int -> [a] -> [a]
lastN n xs = drop (length xs - n) xs

-- Use the largest term less than 4000000 and the next term to calculate the answer
solution :: Integer
solution = div (s - 1) 2
    where
        [a,b] = lastN 2 . takeUntil (> 4000000) $ fibonacci
        s | even b    = a
          | odd a     = b
          | otherwise = a + b
