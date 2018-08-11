##url https://github.com/Avik-Jain/100-Days-Of-ML-Code/blob/master/Code/Day%201_Data%20PreProcessing.md

## step 1
import numpy as np
import pandas as pd

## step 2
##dataset = pd.read_csv('data.csv')
##X = dataset.iloc[ : , :-1].values
##Y = dataset.iloc[ : , 3].values

dataset = pd.read_csv('day1data.csv')
X = dataset.iloc[ : , :-1].values
Y = dataset.iloc[ : , 3].values

## step 3
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = "NAN", strategy = "mean", axis = 0)
imputer = imputer.fit(X[ : , 1:3])
X[ : ,1:3] = imputer.transform(X[ : , 1:3])

## step4
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[ : , 0] = labelencoder_X.fit_transform(X[ : , 0])

onehotencoder = OneHotEncoder(categorical_features= [0])
X = onehotencoder.fit_transform(X).toarray
labelencoder_Y = LabelEncoder()
Y = labelencoder_Y.fit_transform(Y)

## step 5
from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split( X , Y , test_size = 0.2, random_state = 0)

## step6
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)

