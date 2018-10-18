#!/usr/bin/env python3.6

import numpy as np
import numpy.random as rand
import scipy as sp
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk

import scipy.io as spio


def load_mat(filepath, names = None, *kargs, **kwargs):
    filemat = spio.loadmat(filepath, squeeze_me=True, *kargs, **kwargs)

    df = pd.DataFrame(filemat['X'])
    df['anomaly'] = filemat['y'].astype(str)
    df['anomaly'] = df.replace({'anomaly': {'0.0': False,
                                            '1.0': True}})['anomaly'].astype(bool)

    if names:
        df.columns = names + ['anomaly']
    else:
        df.columns = ['X' + str(i) for i in range(1, len(df.columns))] + ['anomaly']

    return(df)
