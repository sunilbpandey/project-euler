module P017.P017 (solution) where

import qualified Data.Map as Map

names = Map.fromList
    [(0, "")
    ,(1, "one")
    ,(2, "two")
    ,(3, "three")
    ,(4, "four")
    ,(5, "five")
    ,(6, "six")
    ,(7, "seven")
    ,(8, "eight")
    ,(9, "nine")
    ,(10, "ten")
    ,(11, "eleven")
    ,(12, "twelve")
    ,(13, "thirteen")
    ,(14, "fourteen")
    ,(15, "fifteen")
    ,(16, "sixteen")
    ,(17, "seventeen")
    ,(18, "eighteen")
    ,(19, "nineteen")
    ,(20, "twenty")
    ,(30, "thirty")
    ,(40, "forty")
    ,(50, "fifty")
    ,(60, "sixty")
    ,(70, "seventy")
    ,(80, "eighty")
    ,(90, "ninety")
    ,(1000, "onethousand")
    ]

numberName :: Int -> String
numberName n =
    case Map.lookup n names of
        Just s  -> s
        Nothing
            | n < 100   -> numberName (n-units) ++ numberName units
            | tens == 0 -> hundreds
            | otherwise -> hundreds ++ "and" ++ numberName tens
            where
                units = mod n 10
                tens = mod n 100
                hundreds = numberName (div n 100) ++ "hundred"

solution :: Integer
solution = (toInteger . sum . map (length . numberName)) [1..1000]
