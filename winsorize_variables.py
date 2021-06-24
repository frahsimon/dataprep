# -*- coding: utf-8 -*-
"""
Created on Thu May 20 15:33:59 2021

@author: frede
"""

def win_fun(df, timev, vars_w, pl, pu):
    '''df = dataframe
    timev = time variable
    vars_w = variable(s) to be winsorized
    p1 = lower percentile
    pu = upper percentile'''

    import pandas
    
    vars_w = [vars_w] if isinstance(vars_w, str) else vars_w
    
    df1 = df.copy()
    timev_list = df1[timev].unique() 
    
    for j in vars_w:
        
        df2 = pandas.DataFrame()
        
        for i in timev_list:

            df3 = df1[(df1[timev] == i)].copy()
            df3['low'] = df3[j].quantile(pl)
            df3['high'] = df3[j].quantile(pu)
            df2 = df2.append(df3)
            
        df2[j] = np.where(df2[j] < df2['low'], df2['low'], df2[j])
        df2[j] = np.where(df2[j] > df2['high'], df2['high'], df2[j])
        df1 = df2
           
    return df1

