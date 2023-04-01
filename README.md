# Factor-Analysis

Introduction 
For this lab, we are going to use the factor analysis technique as feature reduction to reduce the feature in dataset.

Objective
To explore the factors determining the decision of initiating remanufacturing business in India.

The Data
Based on literature survey, 14 issues are identified that make remanufacturing business infeasible for different company.

Describing the data

RangeIndex: 41 entries, 0 to 40
Data columns (total 16 columns):
 #   Column     Non-Null Count  Dtype 
---  ------     --------------  ----- 
 0   SL         41 non-null     int64 
 1   Companies  41 non-null     object
 2   V1         41 non-null     int64 
 3   V2         41 non-null     int64 
 4   V3         41 non-null     int64 
 5   V4         41 non-null     int64 
 6   V5         41 non-null     int64 
 7   V6         41 non-null     int64 
 8   V7         41 non-null     int64 
 9   V8         41 non-null     int64 
 10  V9         41 non-null     int64 
 11  V10        41 non-null     int64 
 12  V11        41 non-null     int64 
 13  V12        41 non-null     int64 
 14  V13        41 non-null     int64 
 15  V14        41 non-null     int64 
dtypes: int64(15), object(1)
memory usage: 5.2+ KB
 

Assessing the Factorability of the Data
Before we go too far down the road with this analysis, we should evaluate the “factorability” of our data. In other words, “are there meaningful latent factors to be found within the data?” We can check two things: 
(1) Bartlett’s test of sphericity. 
(2) The Kaiser-Meyer-Olkin measure of sampling adequacy.

Bartlett’s Test of Sphericity
The most liberal test is Bartlett’s test of sphericity - this evaluates whether or not the variables intercorrelate at all, by evaluating the observed correlation matrix against an “identity matrix” (a matrix with ones along the principal diagonal, and zeroes everywhere else). If this test is not statistically significant, you should not employ a factor analysis.

Chi_square_value =500.8142719899995 
P_value 	    =6.666018861410905e-58
Bartlett’s test was statistically significant, suggesting that the observed correlation matrix among the items is not an identity matrix.

KMO
The Kaiser-Meyer-Olkin (KMO) measure of sampling adequacy is a better measure of factorability. The KMO tests to see if the partial correlations within your data are close enough to zero to suggest that there is at least one latent factor underlying your variables. The minimum acceptable value is 0.60 before undertaking a factor analysis

kmo _model = 0.6670308043222346
The overall KMO for our data is 0.66 which is not excellent – but this suggests that our data is adequate we can go ahead with our planned factor analysis.

Conducting the Factor Analysis
Conduct the factor analysis for 2 factor and without rotation.

factor loading :
[[-0.60866917  	0.64742003]
 [-0.61792639  	0.65063522]
 [ 0.69203744  	0.12495172]
 [ 0.82010948 	-0.0777264 ]
 [-0.57061367  	0.6320802 ]
 [-0.65688813  	0.41553829]
 [-0.42155073  	0.40529052]
 [-0.61573905 	-0.49869244]
 [-0.48500542 	-0.41155195]
 [-0.07805301  	0.6211596 ]
 [ 0.80558257  	0.35419141]
 [ 0.7687813   	0.35594852]
 [ 0.74291608  	0.40626894]
 [ 0.75132408  	0.34456739]]

Here we observed that some of the factor are shows good loading on both the factor , so we have to rotate the  data to overcome this cross loading.



[6.14808269 3.30505941 1.02436621 0.9439278  0.59144416 0.57588844
0.38892042 0.28955435 0.22004001 0.17378175 0.15322265 0.10892026
0.04246395 0.03432789]
 
Based on the condition eigen value more than 1  and scree plot we can say that 3 factor will give the better information about the data.so we again do the factor analysis for 3 factor with varimax rotation.

Conducting the Factor Analysis with rotation
Conduct the factor analysis for 3 factor and with varimax rotation.
	

Factor loading 

[[ 0.83067803 	 0.03757231 	-0.30980941]
 [ 0.85367884	 -0.02107667 	-0.24695863]
 [-0.21505937 	 0.33312034 	 0.62840671]
 [-0.42864236 	 0.2006417  	 0.8151546 ]
 [ 0.88165839 	-0.13423417	 -0.05463433]
 [ 0.73243054	 -0.27780006 	-0.18033244]
 [ 0.54598605	 -0.00983849 	-0.2057894 ]
 [-0.03283996	 -0.81770855	 -0.26406936]
 [-0.00886216 	-0.7870915  	-0.0722381 ]
 [ 0.60373527  	0.15741991  	0.23714632]
 [-0.150864    	0.70875139  	0.49680209]
 [-0.0735029   	0.52619032  	0.68407915]
 [-0.07879194  	0.70989822  	0.45694169]
 [-0.0811026   	0.53091272  	0.64158134]]

Variance explained by the three factors

Factor	Total	% of variance	Cumulative %
1	3.66725683	26.194692	26.194692
2	3.12634055	22.331004	48.525696
3	2.7605847	19.718462	68.244158

Inference 

Here we only get the 68.24% percentage of variance of data , approximately 32 % information are lost this will not adequate, so we need improve the number of factor to gain more information. 


Conducting the Factor Analysis with rotation – n_factor =5

Conduct the factor analysis for 5 factor and with varimax rotation.


Factor loading 
[[ 0.00459332  0.85934949 -0.22899232  0.23087051  0.15113714]
 [-0.07178869  0.95536368 -0.12930198  0.18538056  0.16419123]
 [ 0.30568408 -0.21409058  0.61946924 -0.28765649  0.20785276]
 [ 0.22660877 -0.40335168  0.80074753 -0.15330987 -0.08861893]
 [-0.05945849  0.57471534 -0.10800377  0.64416509  0.27628453]
 [-0.19730875  0.41570958 -0.23967218  0.72168821  0.2034681 ]
 [-0.03874284  0.42605693 -0.24010156  0.06940445  0.43835875]
 [-0.80923061 -0.0517938  -0.24169947  0.08131146 -0.03583929]
 [-0.77763725 -0.01199556 -0.02129218  0.13442116 -0.10761589]
 [ 0.1564218   0.28662605  0.16937486  0.22289972  0.79512682]
 [ 0.7186437  -0.20854929  0.41506837 -0.19516364  0.20970798]
 [ 0.52529408 -0.04390022  0.68842719 -0.13582274  0.05117418]
 [ 0.7993389  -0.10487864  0.41137175  0.09805065 -0.1426645 ]
 [ 0.60401273 -0.12968772  0.63140952  0.1414682  -0.12680189]]

Variance explained by the five factors
Factor	Total	% of variance	Cumulative %
1	3.27413442 	23.386674 	23.386674 
2	2.70258481	19.304177	42.690852
3	2.52252985	18.01807	60.708922
4	1.29504557	9.250326	69.959247
5	1.13886849	8.134775	78.094022



Inference 

Here we got 78.09 % of cumulative variance explained by all 5 factor, we loss approximately 12 % information from the original data but this one adequate amount information further any analysis.


Conclusion 
The dataset has probably governed by the five underlying factors
