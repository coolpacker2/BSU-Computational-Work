import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("RealEstateUnitedStates.csv")


X = data["Median Income - Current Dollars"]
y = data["Average Sales Price"]

#Calculate mean of X and y
X_mean = np.mean(X)
y_mean = np.mean(y)

#Total number of observations
n = len(X)

#Calculate slope (m) and intercept (b)
numerator = np.sum((X - X_mean) * (y - y_mean))
denominator = np.sum((X - X_mean) ** 2)
m = numerator / denominator
b = y_mean - m * X_mean

#Plot the original data
plt.scatter(X, y, color="b", marker="o", s=30, label="Data Points")

#Plot the regression line
plt.plot(X, m*X + b, color="r", label="Regression Line")

#Add labels and legend
plt.xlabel('Median Income - Current Dollars')
plt.ylabel('Average Sales Price')
plt.legend()

#Show plot
plt.show()

#Print the equation of the regression line
print("Equation of the regression line: y =", round(m, 2), " X +", round(b, 2))
