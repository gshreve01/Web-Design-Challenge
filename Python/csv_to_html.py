# -*- coding: utf-8 -*-
"""
Created on Fri May 22 04:46:10 2020

@author: gshre
"""


import pandas as pd

csvFile = "../WebVisualizations\Resources/Merged_df.csv"

df = pd.read_csv((csvFile))
df = df[['County', 'Population','Median Age', 'Household Income',
         'Per Capita Income', 'Confirmed', 'Deaths', 'Latitude', 'Longitude']]
df.to_html(open('data_table.html', 'w'), index=False, border=0)
# html = df.to_html(index=False)
# print(html)