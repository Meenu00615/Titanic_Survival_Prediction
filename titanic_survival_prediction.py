# -*- coding: utf-8 -*-
"""Titanic_Survival_Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-92N2GSe90twI3iXm32cwo2CrMEuKnsf

##**Importing libraries**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn import preprocessing

"""##**Data Collection and Preprocessing**"""

titanic_dataset=pd.read_csv("/content/train.csv")  #csv to pandas DataFrame

#First five rows from DataFframe
titanic_dataset.head(5)

#SibSp-#Sibiling/Spouse
#Parch-Parent /Children

#shape of the dataset
titanic_dataset.shape   #Rows*Columns

titanic_dataset.describe() #Sattistical measure of the Titanic dataset

titanic_dataset.info()   #NaN are the missing values

#missing values in each column
titanic_dataset.isnull().sum()

"""###**Handling the missing values in the Titanic Dataset**"""

titanic_dataset=titanic_dataset.drop(columns=['Cabin'], axis=1)

titanic_dataset['Age'].fillna(titanic_dataset['Age'].mean(), inplace=True)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Now, when you print the DataFrame, it will display all rows and columns
print(titanic_dataset['Age'])

titanic_dataset['Age'].dtype

#droping cabin column from the dataset

titanic_dataset.head()

titanic_dataset.head()

#Replacing all the missing values with the mean value

titanic_dataset['Age'].mean()

titanic_dataset['Age'].fillna(titanic_dataset['Age'].mean, inplace=True)

titanic_dataset['Age'].dtypes

#mode value of embarked column
print(titanic_dataset['Embarked'].mode())

print(titanic_dataset['Embarked'].mode()[0])

#replacing the missing value with the embarked columns' mode value

titanic_dataset['Embarked'].fillna(titanic_dataset['Embarked'].mode()[0], inplace =True)

titanic_dataset.isnull().sum()  #Now no missing value is presint in the dataaset

"""#Data Analysis"""

titanic_dataset['Survived'].value_counts()

"""###***Data Visualization***"""

sns.set()

import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x='Sex', data=titanic_dataset) #count plot for the sex column

sns.countplot(x='Survived', data=titanic_dataset)  #count plot for the Survived column

sns.countplot(x='Sex', hue='Survived', data=titanic_dataset)

sns.countplot(x='Pclass', data=titanic_dataset)

#C = Cherbourg, Q = Queenstown, S = Southampton

titanic_dataset['Embarked'].value_counts()

#converting dataset's categorical data into the numerical data

"""###***Dividing the dataset into feature and the target values***"""

titanic_dataset.replace({'Sex':{'male':0, 'female':1}, 'Embarked':{'S':0, 'C':1, 'Q':2}}, inplace=True)

X=titanic_dataset.drop(columns = ['PassengerId', 'Name', 'Ticket', 'Survived'], axis=1)
Y=titanic_dataset['Survived']

titanic_dataset.head()

print(X.head())

"""###***Spliting the dataset into the training and testing dataset***"""

titanic_dataset.head()



"""###***Training the model***"""

# prompt: find what is the problem in the above X and Y training?

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
print(X.shape, X_train.shape, X_test.shape)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

X.head()

titanic_dataset.describe()

titanic_dataset.info()

titanic_dataset['Age'] = pd.to_numeric(titanic_dataset['Age'], errors='coerce')
titanic_dataset['Age'] = titanic_dataset['Age'].astype('float')

X_train.head()

print(X.shape, X_train.shape, X_test.shape)

print(X_train.dtypes)

print(Y_train.dtypes)

titanic_dataset['Age'].dtypes

pd.set_option('display.max_colwidth', None)

print(titanic_dataset['Age'])

model=LogisticRegression()
model.fit(X_train, Y_train)

"""###***Model Evaluation***"""

#Accuracy Score
#Checking accuracy of the training dataset
X_train_prediction=model.predict(X_train)

print(X_train_prediction)

training_data_accuracy=accuracy_score(Y_train, X_train_prediction)

print("Acc_score_of_the_training_data", training_data_accuracy)

#Now checking the accuracy on the test data

X_test_prediction=model.predict(X_test)
print(X_test_prediction)

testing_data1_accuracy=accuracy_score(Y_test, X_test_prediction)
print("Accuracy of the test data", testing_data1_accuracy)