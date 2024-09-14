module P015.P015 (solution) where

import ProjectEuler.Common (fac)

solution :: Integer
solution = div (fac 40) ((fac 20) * (fac 20))
