#House Price Prediction using Regression

#Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

house = pd.read_csv("data/train.csv")

#Exploratory Data Analysis
house.head()
house.shape

house.info()
house.describe()

#Histogram
plt.figure(figsize = (10, 6))

sns.histplot(data = house, x= "SalePrice", bin= 30)

plt.title("Distribution of House Sale Prices")
plt.xlabel("Sale Price")
plt.ylabel("Frequency")

plt.show()

#Boxplot
plt.figure(figsize = (8, 5))

plt.boxplot(x= house["SalePrice"])

plt.title("Box Plot of Sale Price")

plt.show()
