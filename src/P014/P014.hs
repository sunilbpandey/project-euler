module P014.P014 (solution) where

import qualified Data.Map as Map
import Data.List (maximumBy)
import Data.Ord (comparing)

type Cache = Map.Map Int Int

collatzNext :: Int -> Int
collatzNext n = if even n then div n 2 else 3 * n + 1

getOrAdd :: Int -> Cache -> (Int, Cache)
getOrAdd n cache =
    case Map.lookup n cache of
        Just l  -> (l,cache)
        Nothing -> let (l,cache') = getOrAdd (collatzNext n) cache in (l+1, (Map.insert n (l+1) cache'))

lengths :: Int -> Int -> Cache -> [(Int, Int)]
lengths n limit cache
    | n == limit = []
    | otherwise  = let (l,cache') = getOrAdd n cache in (n,l):(lengths (n+1) limit cache')

solution :: Integer
solution = toInteger . fst . maximumBy (comparing snd) $ lengths 500000 1000000 (Map.fromList [(1, 1)])
