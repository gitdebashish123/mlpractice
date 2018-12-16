#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 18:30:20 2018

@author: debashish.kheti
"""

import pandas as pd

df = pd.DataFrame({'Days':[1,2,3,4],'Vistors':[5000,2000,4000,9000]})
print(df)

df = df.rename(columns={'Vistors':'Users'})
print(df)


data = pd.read_csv(r"/Users/debashish.kheti/Desktop/ML/Day-1/inputs/regiment.csv")
print(data)

data.to_html("/Users/debashish.kheti/Desktop/ML_Home/output_files/regiment.html")