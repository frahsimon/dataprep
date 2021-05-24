# -*- coding: utf-8 -*-
"""
Created on Mon May 24 11:17:43 2021

@author: frede
"""

def scale_var(df, vars_sc, scaler):
    # This function takes a dataframe and scales a selection of its variables
    # by a scaling variable which is either an integer, float or a column of 
    # the dataframe.
    # df = dataframe
    # var_sc = variable to be scaled
    # scaler = scaling variable (integer, float or string (string indicating
    # that the scaler is a column of the dataframe))
    
    _temp_df = df.copy()
    
    vars_sc = [vars_sc] if isinstance(vars_sc, str) else vars_sc
    
    if isinstance(scaler, int) or isinstance(scaler, float):
        for i in vars_sc:
             _temp_df[i] = _temp_df[i] / scaler
    else:
        for i in vars_sc:
            _temp_df[i] = _temp_df[i] / _temp_df[scaler]
        
    return _temp_df



