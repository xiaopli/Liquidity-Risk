import numpy as np
import math
from math import sqrt
import pandas as pd
import numpy.random as npr
import matplotlib.pyplot as plt
import os 

pdf = pd.read_excel (r'C:\Users\gcvpi\Desktop\SACHAPSQq118q119V3.xlsx')

def get_est(x, sample_size=1):
    bal1 = 0
    deb1 = 0
    if x.csigma1 > 0:
        dpois1 = npr.poisson(x.dlam1, size=sample_size)
        cpois1 =npr.poisson (x.clam1, size=sample_size)
        corrdpois1 = ((cpois1 * x.corr11) + sqrt((1-x.corr11)**2) * dpois1)
        dn1 = npr.normal(x.dmu1, x.dsigma1, sample_size)
        dn_use = max (dn1, 0)
        cn1 = npr.normal(x.cmu1, x.csigma1, sample_size)
        cn_use = max(cn1, 0)
        cred1 = x.clam1 *cn_use
        deb1 = corrdpois1 * dn_use
        bal1 = cred1 - deb1
    return bal1
bal_array = []
for i in list (range(10000)):
    pdf.loc[:, 'gil_bal']= pdf.apply(lambda x:get_est(x), axis=1)
    pdf['cumsum_gil_bal'] = pdf['gil_bal'].cumsum()
    my_min = pdf['cumsum_gil_bal'].min()
    bal_array.append(my_min)
    
bal_array = np.array(bal_array)
print("95th percentile : ${:,.0f}".format(np.percentile(bal_array,5)))
print("96th percentile : ${:,.0f}".format(np.percentile(bal_array,4)))
print("97th percentile : ${:,.0f}".format(np.percentile(bal_array,3)))
print("98th percentile : ${:,.0f}".format(np.percentile(bal_array,2)))
print("99th percentile : ${:,.0f}".format(np.percentile(bal_array,1)))


