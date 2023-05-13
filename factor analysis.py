# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 20:38:54 2022

@author: Asish
"""

# Import libaries
import pandas as pd
from factor_analyzer import FactorAnalyzer
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\ADMIN\Desktop\MBA - BA II\Multivariate analysis lab\2.factor analysis\testdata.csv")
df.info()
#Preprocess Data
df.columns
# Dropping unnecessary columns
df.drop(['SL', 'Companies'], axis = 1, inplace=True)
# Dropping missing values rows
df.dropna(inplace=True)
df.info()
df.head()

#Bartlett’s Test
from factor_analyzer.factor_analyzer import calculate_bartlett_sphericity
chi_square_value,p_value= calculate_bartlett_sphericity(df)
print(chi_square_value, p_value)

#Kaiser-Meyer-Olkin (KMO) Test
from factor_analyzer.factor_analyzer import calculate_kmo
kmo_all,kmo_model=calculate_kmo(df)
print(kmo_model)

# Create factor analysis object and perform factor analysis
fa = FactorAnalyzer(n_factors = 2, rotation=None)
fa.fit(df)
print(fa.loadings_)
# Check Eigenvalues
ev, v = fa.get_eigenvalues()
print(ev)
# Create scree plot using matplotlib
plt.scatter(range(1,df.shape[1]+1),ev)
plt.plot(range(1,df.shape[1]+1),ev)
plt.title('Scree Plot')
plt.xlabel('Factors')
plt.ylabel('Eigenvalue')
plt.grid()
plt.show()

# Create factor analysis object and perform factor analysis
fa = FactorAnalyzer(n_factors = 3, rotation="varimax")
fa.fit(df)
print(fa.loadings_)

# Get variance of each factors
fa.get_factor_variance()

# Create factor analysis object and perform factor analysis
fa = FactorAnalyzer(n_factors = 5, rotation="varimax")
fa.fit(df)
print(fa.loadings_)

# Get variance of each factors
fa.get_factor_variance()
