#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 23:18:30 2018

@author: debashish.kheti
"""

#Problem Statement : Percentage of unemployment youth for every country from 2010-11

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use("fivethirtyeight")

country = pd.read_csv("/Users/debashish.kheti/Desktop/ML_Home/input_files/API_ILO_country_YU.csv",index_col=0)

df = country.head(5)
df = df.set_index(["Country Code"])
print(df)
df = df.reindex(columns=["2010","2011"])
print(df)

db = df.diff(axis=1)

db.plot(kind = 'bar')
plt.show