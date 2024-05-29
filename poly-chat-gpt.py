import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("RealEstateUnitedStates.csv")

X = data["Median Income - Current Dollars"]
y = data["Average Sales Price"]

# θ=((X^T)*X)^−1*(X^T)*y is main formula derived from linear regression algorithm
# Define the degree of the polynomial
degree = 10

# X_poly represents the matrix of polynomial features
X_poly = np.column_stack([X ** i for i in range(1, degree + 1)])
#using column stack to turn it into a 2d array used later, when we make it into a 2d array, we can replace X with X_Poly

# the for loop creates multiple different arrays which are going to be stacked
# it is stacking a bunch of 1d horizontal arrays made by a for loop with each layer representing a different power to make a big 2d array in layman terms

# θ=((X^T)*X)^−1*(X^T)*y
# Fit polynomial regression model

coefficients = np.linalg.inv(X_poly.T.dot(X_poly)).dot(X_poly.T).dot(y)
#Least squares algorithm θ=((X^T)*X)^−1*(X^T)*y basically the above thing is finding the vector coefficient using the algebra function from the numpy library 
#things to notice
#1 we inverse it to get ((X^T)*X)^−1
#2 dot means multiplying arrays
#3 .T is transpose which switchs columns with rows and rows with columns (now the power is horizanl and the numbers are vertical) we do this to 
# Plot the original data
#4 essentially we just transpose the data which is the ^T in the formula multiplied by the normal x non transposed and then we multiply the rest
#which is x transposed again and y making θ=((X^T)*X)^−1*(X^T)*y
#they are just calculating the components to plug into the equation for the vector coefficients there are multiple of them because you are multiplying
#matrices which contain multiple values in the table
#5 these coefficients are used to make the multiple different lines on the graph

plt.scatter(X, y, color="b", marker="o", s=30, label="Data Points")

# Predictions
y_pred = X_poly.dot(coefficients)
# we multiply the coefficient matrix and the x poly matrix to get y predict
# the formula is adding all thetas multiplied by x^n power
# Sort X and predictions for plotting
# now we have multiple accurate y values in an array that can be plotted

sorted_indices = np.argsort(X)
X_sorted = X[sorted_indices]
y_pred_sorted = y_pred[sorted_indices]
#indices just organize things from least to greatest so that now we can plot it point for point instead of hopping all over the place
#otherwise we would get some random shit, we are just making sure the x values align with the y values from least to greatest
# Plot the regression line
plt.plot(X_sorted, y_pred_sorted, color="r", label="Polynomial Regression")
#now it is plotting each of the x and y values of the array and since we organized it, it will form a line that goes in a "good direction"
# Add labels and legend
plt.xlabel('Median Income - Current Dollars')
plt.ylabel('Average Sales Price')
plt.legend()

# Show plot
plt.show()

# Print the equation of the polynomial regression line
equation = "y = "
for i, coef in enumerate(coefficients):
    if i == 0:
        equation += str(coef) # converting to string
    else:
        equation += f" + ({coef} * X^{i})"
print("Equation of the polynomial regression line:", equation)

#enumarate generates tuples, the equation will look something like "coeffx^6+coeffx^5" because thats just how polynomials work
#like this part is trying to just use coeffs to generate each of the weaker powers after
#in summary we are basically just following the formula using this:
#x will be a matrix layered by multiple types of powers
#then we calculate vector coefficient to figure out the direction of the line
#then we get some y values using the vector coeffient and the layers of powers  (x)