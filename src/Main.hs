module Main where

import Data.Maybe (fromJust)
import System.Environment (getArgs)

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
    ]

main :: IO ()
main = do
    (problem:_) <- getArgs
    print $ fromJust $ lookup problem dispatch
