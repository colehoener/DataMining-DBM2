import pandas as pd
import numpy as np

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nPreprocessing and cleaning data...\n")
##Read excel spread sheet of data
data = pd.read_excel('cleaned_data.xls', header=None)

##Declare the column names
data.columns = ['date', 's_and_p_comp', 'dividend', 'earnings',
                'CPI', 'fraction_date', 'long_interest_rate', 'real_price',
                'real_dividend', 'real_total_return_price','real_earnings',
                'real_scaled_earnings', 'CAPE', 'TR_CAPE', 'excess_CAPE', 'montly_bond_return',
                'real_bond_return','10_year_stock_return', '10_year_bond_return',
                '10_year_excess_return']

##Drop all rows with missing data
data = data.replace('NA',np.NaN)

data.head()

##Drop "10 year" columns so there are no rows with missing data after 2011
print("Dropping unfinished columns...")    
data = data.drop(['10_year_stock_return'],axis=1)
data = data.drop(['10_year_bond_return'],axis=1)
data = data.drop(['10_year_excess_return'],axis=1)

##Drop rows with missing data
print("Dropping unfinished rows...")
print('\n\nNumber of rows in original data = %d' % (data.shape[0]))
data = data.dropna()
print('Number of rows after discarding missing values = %d\n' % (data.shape[0]))

##Check to make sure there are no missing values in each column
print('Number of missing values:')
for col in data.columns:
    print('\t%s: %d' % (col,data[col].isna().sum()))

print("\n\nPreprocessing done.")