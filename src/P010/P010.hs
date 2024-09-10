module P010.P010 where

import ProjectEuler.PrimeUtils (primesUpTo)

solution :: Integer
solution = (toInteger . sum . primesUpTo) 1999999
