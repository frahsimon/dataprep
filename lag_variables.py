# -*- coding: utf-8 -*-
"""
Created on Thu May 20 09:40:01 2021

@author: frede
"""

def lag_variables(df, idv, timev, varl, lag):
    # This function takes a dataframe and lags a pre-specified selection of its
    # variables.
    # df = dataframe
    # idv = id variable (string variable)
    # timev = time variable (string variable)
    # varl = (list of) variable(s) to be lagged (string or list)
    # lag = (list of) lag(s) (integer or list)
    
    if isinstance(lag, int):
        
        _temp = df
        
        if isinstance(varl, str):
            _temp_list = [idv, timev, varl]
        else:
            _temp_list = varl.copy()
            _temp_list.extend((idv, timev))
                
        _temp2 = _temp[_temp_list]
    
        _temp2[timev + '_lag' + str(lag)] = _temp2[timev] + lag
        _temp2 = _temp2.drop([timev], axis=1)
        
        _temp = _temp.merge(_temp2, 
                             left_on=[idv, timev], 
                             right_on=[idv, timev + '_lag' + str(lag)], 
                             how='left', 
                             suffixes=('', '_lag' + str(lag)))
    
        _temp[timev + '_lag' + str(lag)] = _temp[timev + '_lag' + str(lag)] - lag
        _temp = _temp.sort_values([idv, timev], ascending = [True, True])
        
        return(_temp)
        
    else:
        
        _temp = df
        
        for i in lag:        
        
            if isinstance(varl, str):
                _temp_list = [idv, timev, varl]
            else:
                _temp_list = varl.copy()
                _temp_list.extend((idv, timev))
                    
                _temp2 = _temp[_temp_list]
    
            _temp2[timev + '_lag' + str(i)] = _temp2[timev] + i
            _temp2 = _temp2.drop([timev], axis=1)
        
            _temp = _temp.merge(_temp2, 
                                 left_on=[idv, timev], 
                                 right_on=[idv, timev + '_lag' + str(i)], 
                                 how='left', 
                                 suffixes=('', '_lag' + str(i)))
            
            _temp[timev + '_lag' + str(i)] = _temp[timev + '_lag' + str(i)] - i
            _temp = _temp.sort_values([idv, timev], ascending = [True, True])
        
        return(_temp)
    

