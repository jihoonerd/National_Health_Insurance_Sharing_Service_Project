# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 20:20:00 2017

@author: Jihoon_Kim
"""


# Load Modules
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import dask.dataframe as dd
from dask.diagnostics import ProgressBar
pbar = ProgressBar()
pbar.register()

# Load Data
gj = dd.read_csv('./data/NHIS_OPEN_GJ_2015.CSV')  # Medical Examination Data
t20 = dd.read_csv('./data/NHIS_OPEN_T20_2015.CSV')  # Treatment Data
t60_part1 = dd.read_csv('./data/NHIS_OPEN_T60_2015_part1.CSV')
t60_part2 = dd.read_csv('./data/NHIS_OPEN_T60_2015_part2.CSV')
t60 = t60_part1.append(t60_part2)  # Prescription Data


# Example
sns.countplot(gj.HEIGHT.compute())  # Height Distribution

# Count TOP 10 Main Sick
main_sick_count = t20.MAIN_SICK.value_counts().compute()
top10_main_sick = main_sick_count[:10]

# t20 table confined to top 10 main sick:
t20_top10_sick = t20[t20.MAIN_SICK.isin(top10_main_sick.index)].compute()
sns.countplot(x="MAIN_SICK", hue="SEX", data=t20_top10_sick)
