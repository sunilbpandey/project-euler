module P020.P020 (solution) where

import ProjectEuler.Common (digitSum, fac)

solution :: Integer
solution = digitSum $ fac 100
