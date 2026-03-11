# House Price Prediction using Linear Regression

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    "Area": [500, 800, 1000, 1200, 1500],
    "Price": [50, 80, 100, 120, 150]
}

df = pd.DataFrame(data)

# Feature and Target
X = df[['Area']]
y = df['Price']

# Model
model = LinearRegression()
model.fit(X, y)

# Prediction
area_to_predict = np.array([[1250]])
predicted_price = model.predict(area_to_predict)

print("Predicted House Price for 1250 sqft:", predicted_price[0], "Lakhs")

# Graph
plt.scatter(X, y, color='blue', label='Actual Prices')
plt.plot(X, model.predict(X), color='red', label='Regression Line')

plt.xlabel("House Size (sqft)")
plt.ylabel("House Price (Lakhs)")
plt.title("House Price Prediction using Linear Regression")
plt.legend()

plt.show()
