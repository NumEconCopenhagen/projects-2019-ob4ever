#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '../projects-2019-ob4ever/dataproject'))
	print(os.getcwd())
except:
	pass

#%%
#Importer vigtige pakker
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader as pdr
import pandas_datareader.data as web

import datetime
import pydst
dst = pydst.Dst(lang='da')


#%%
# a. loading data
dst.get_variables('NABP10') # command to se 'id'
dst.get_variables('NABP10').iloc[0]['values'] # command to se 'values' in 'TRANSAKT'

na10 = dst.get_data(table_id = 'NABP10', variables={'TRANSAKT':['B1GD','D1D'],'BRANCHE':['*'], 'PRISENHED':['*'], 'TID':['*']})
na10.tail()


#%%



