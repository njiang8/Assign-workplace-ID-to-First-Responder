# Get-wrkID
Get the wrkID of the First responsors in our study area. Hence, we use synthesized workplace data and real first responsor data.
## Data (.csv file):
* synthesized workplace with workID
* synthesized population data with workID
* real first responsor (eg, hospital, fire station, and police station)

First of all, we should konw the amount of population in ach workplace, we use the population data to calculate

## Ptyhon Package
```
import pandas as pd

import numpy as np

import geopy
```

## What are those code?
* Step 1: to claen up the data and get the coordinate of (lat, long) for furture calculation.
* Step 2: Calculate distance based on the coordinate.
* Step 3: Get the popualtion for each WorkID
* Step 4: Get the WorkID for Hos, Fire, and Police station

## Things to improve

* I need to make each step as fuction, which will be much easier to use.
