import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Least Squares Linear Regression Algorithm
# Degree = 1

# Find a dataset (x and y variables)
# Write the regession
# Plot the regression (whatever you think is applicable)
data = pd.read_csv("usa_mercedes_benz_prices.csv")
#read the price and rating and x = price and y = rating
x_total = 0
y_total = 0

for i in range(len(data["Price"])):
    price_str = data["Price"][i].replace("$","").replace(",","")
    rating_str = data["Rating"][i]
    if price_str != 'Not Priced' and not np.isnan(rating_str):
        x_total = x_total + int(data["Price"][i].replace("$","").replace(",",""))
        y_total = y_total + data["Rating"][i]
x_avg = x_total/len(data["Price"])
y_avg = y_total/len(data["Rating"])
print(x_avg)
print(y_avg) 
#plot points
for i in range(len(data["Price"])):
    x = data["Price"][i].replace("$","").replace(",","")
    y = data["Rating"][i]
    plt.plot(x, y, marker="o", markersize=1, markeredgecolor="red")

#plot line now

n = 1000 # number of points
m = (n * (x_avg * y_avg) - x_total * y_total) / (n * (x_avg ** 2) - x_total ** 2)
b = (y_avg - m * x_avg) / n



x_eq = [0, len(data["Price"])]  # Adjust the range as per your data
y_eq = [m * x + b for x in x_eq]
plt.plot(x_eq, y_eq, '-r', label='Line Of Regression')
plt.show()

