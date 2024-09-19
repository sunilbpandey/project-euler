module P010.P010 (solution) where

import ProjectEuler.PrimeUtils (primesUpTo)

solution :: Integer
solution = (toInteger . sum . primesUpTo) 1999999
