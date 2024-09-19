{-# LANGUAGE DeriveGeneric #-}
{-# LANGUAGE OverloadedStrings #-}

module Main where

import Data.Aeson
import Data.Maybe (fromJust)
import GHC.Generics
import System.Console.GetOpt
import System.Environment (getArgs)
import System.Exit
import qualified Data.ByteString.Lazy as BL

import qualified P001.P001 as P001 (solution)
import qualified P002.P002 as P002 (solution)
import qualified P003.P003 as P003 (solution)
import qualified P004.P004 as P004 (solution)
import qualified P005.P005 as P005 (solution)
import qualified P006.P006 as P006 (solution)
import qualified P007.P007 as P007 (solution)
import qualified P008.P008 as P008 (solution)
import qualified P009.P009 as P009 (solution)
import qualified P010.P010 as P010 (solution)
import qualified P011.P011 as P011 (solution)
import qualified P012.P012 as P012 (solution)
import qualified P013.P013 as P013 (solution)
import qualified P014.P014 as P014 (solution)
import qualified P015.P015 as P015 (solution)
import qualified P016.P016 as P016 (solution)
import qualified P017.P017 as P017 (solution)
import qualified P018.P018 as P018 (solution)
import qualified P019.P019 as P019 (solution)
import qualified P020.P020 as P020 (solution)
import qualified P021.P021 as P021 (solution)
import qualified P022.P022 as P022 (solution)

dispatch :: [(String, Integer)]
dispatch =
    [("1", P001.solution)
    ,("2", P002.solution)
    ,("3", P003.solution)
    ,("4", P004.solution)
    ,("5", P005.solution)
    ,("6", P006.solution)
    ,("7", P007.solution)
    ,("8", P008.solution)
    ,("9", P009.solution)
    ,("10", P010.solution)
    ,("11", P011.solution)
    ,("12", P012.solution)
    ,("13", P013.solution)
    ,("14", P014.solution)
    ,("15", P015.solution)
    ,("16", P016.solution)
    ,("17", P017.solution)
    ,("18", P018.solution)
    ,("19", P019.solution)
    ,("20", P020.solution)
    ,("21", P021.solution)
    ,("22", P022.solution)
    ]

data Flag = Test deriving (Eq)

options :: [OptDescr Flag]
options =
    [Option ['t'] ["test"] (NoArg Test) "test the solution"
    ]

parseArgs :: [String] -> IO ([Flag], String)
parseArgs argv =
    case getOpt Permute options argv of
        (args, p:_, []) -> return (args, p)
        (_, _, err)     -> do
            putStrLn (concat err)
            exitWith (ExitFailure 1)

data Record = Record { problem :: Int, answer :: String } deriving (Generic, Show)

instance FromJSON Record

loadAnswers :: BL.ByteString -> [(Int, String)]
loadAnswers contents = map parseRecord $ fromJust (decode contents :: Maybe [Record])
    where
        parseRecord (Record p a) = (p,a)

solve :: String -> String
solve = show . fromJust . flip lookup dispatch

lookupAnswer :: [(Int, String)] -> String -> String
lookupAnswer answers = fromJust . flip lookup answers . read

test :: [(Int, String)] -> String -> String
test answers p =
    if expected == actual
        then "PASS"
        else "FAIL: " ++ expected ++ " /= " ++ actual
    where
        expected = lookupAnswer answers p
        actual = solve p

exec :: ([Flag], String) -> IO String
exec (args, p) = do
    if Test `elem` args
        then do
            contents <- BL.readFile "src/answers.json"
            let answers = loadAnswers contents
            return $ test answers p
        else
            return $ solve p

main :: IO ()
main = getArgs >>= parseArgs >>= exec >>= putStrLn
