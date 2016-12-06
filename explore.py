import pandas as pd


data_path = '/Users/ajith/bigdata/git_codes/microfinance/Data/demographics/'
fil_name = data_path+'individual_characteristics.dta'
df = pd.read_stata(fil_name)

import numpy as np
data_path = '/Users/ajith/bigdata/git_codes/microfinance/Data/network_data/adj_mat/'
fil_name = data_path+'adj_allVillageRelationships_HH_vilno_64.csv'
csv = np.genfromtxt(fil_name,delimiter = ',')