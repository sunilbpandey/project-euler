module P022.P022 (solution) where

import Data.Char (ord)
import Data.List (sort)
import System.IO.Unsafe (unsafePerformIO)

ltrim :: Eq a => a -> [a] -> [a]
ltrim ch = dropWhile (== ch)

rtrim :: Eq a => a -> [a] -> [a]
rtrim ch = reverse . ltrim ch . reverse

trim :: Eq a => a -> [a] -> [a]
trim ch = rtrim ch . ltrim ch

splitOn :: Char -> String -> [String]
splitOn ch s = case ltrim ch s of
                "" -> []
                s' -> h : splitOn ch t
                    where (h, t) = break (== ch) s'

names :: String -> [String]
names = map (trim '"') . splitOn ','

letterValue :: Char -> Int
letterValue = (+ 1) . (subtract (ord 'A')) . ord

nameValue :: String -> Int
nameValue = sum . (map letterValue)

nameScores :: String -> [Int]
nameScores = zipWith (*) [1..] . map nameValue . sort . names

solution :: Integer
solution = toInteger . sum . nameScores . unsafePerformIO . readFile $ "src/P022/p022_names.txt"
