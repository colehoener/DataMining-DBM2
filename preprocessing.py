import pandas as pd
import numpy as np

data = pd.read_excel('cleaned_data.xls', header=None)

data.columns = ['date', 's_and_p_comp', 'dividend', 'earnings',
                'CPI', 'fraction_date', 'long_interest_rate', 'real_price',
                'real_dividend', 'real_total_return_price','real_earnings',
                'real_scaled_earnings', 'CAPE', 'TR_CAPE', 'excess_CAPE', 'montly_bond_return',
                'real_bond_return','10_year_stock_return', '10_year_bond_return',
                '10_year_excess_return']
                
data = data.drop(['10_year_stock_return'],axis=1)
data = data.drop(['10_year_bond_return'],axis=1)
data = data.drop(['10_year_excess_return'],axis=1)
data = data.replace('NA',np.NaN)

data.head()

print('Number of instances = %d' % (data.shape[0]))
print('Number of attributes = %d' % (data.shape[1]))

print('Number of missing values:')
for col in data.columns:
    print('\t%s: %d' % (col,data[col].isna().sum()))

print('Number of rows in original data = %d' % (data.shape[0]))
data2 = data.dropna()
print('Number of rows after discarding missing values = %d' % (data2.shape[0]))