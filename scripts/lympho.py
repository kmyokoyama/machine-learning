#!/usr/bin/env python3.6

import numpy as np
import numpy.random as rand
import scipy as sp
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk

import data_io
import string

from importlib import reload

reload(data_io)

lympho = data_io.load_mat("../data/lympho.mat", names = None)

type(lympho)
print(lympho.head())
print(lympho.loc[:, ['X1', 'X2', 'X3', 'X4', 'anomaly']].head(10))

print(lympho.info())
print(lympho.describe())

print(lympho['anomaly'].value_counts())
print(pd.crosstab(index=lympho['anomaly'], columns="count"))
