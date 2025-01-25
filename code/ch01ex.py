
# import necessary packages for project
from __future__ import print_function, division

import numpy as np 
import sys

import nsfg
import thinkstats2

# Read in data set
def ReadFemResp(dict_file='2002FemResp.dict',
                data_file='2002FemResp.dat.gz',
                nrows = None):
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(data_file, compression = 'gzip', nrows = nrows)
    CleanFemResp(df)
    return df

def CleanFemResp(df):
    return df
# function that validates pregnancy numbers
def ValidatePregnum(resp):
    preg = nsfg.ReadFemPreg()
# makes the map of case id's to  list of pregnancy indices
    preg_map = nsfg.MakePregMap(preg)
    
    for index, pregnum in resp.pregnum.items():
        caseid = resp.caseid[index]
        indices = preg_map[caseid]
    # check to see if the pregnum from respondent files equals
    # the number of files in the pregnancy file    
        if len(indices) != pregnum:
            return False
        
    return True

# tests the functions in the files
def main(script):
    
    resp = ReadFemResp()
    
    assert(len(resp) == 7643)
    assert(resp.pregnum.value_counts()[1] == 1267)
    assert(ValidatePregnum(resp))
    
    print('%s: All Tests Passed.' % script)
    
if __name__ == '__main__':
    main(*sys.argv)
    
    