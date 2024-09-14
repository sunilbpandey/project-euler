module P019.P019 (solution) where

import qualified Data.Map as M

data Weekday = Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday deriving Eq

dayOfWeek :: Int -> Int -> Int -> Weekday
dayOfWeek year month day = weekday M.! (mod (day + (div (13 * (m + 1)) 5) + y + (div y 4) - (div y 100) + (div y 400)) 7)
    where
        m = if month > 2 then month else month + 12
        y = if month > 2 then year else year - 1
        weekday = M.fromList $ zip [0..6] [Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday]

count :: Eq a => a -> [a] -> Int
count x = length . filter (== x)

solution :: Integer
solution = toInteger $ count Sunday [dayOfWeek y m 1 | y <- [1901..2000], m <- [1..12]]
