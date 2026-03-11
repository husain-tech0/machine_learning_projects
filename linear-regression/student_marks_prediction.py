import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = {
    "study_hours":[1,2,3,4,5],
    "marks":[30,40,50,60,70]
}

df = pd.DataFrame(data)

X = df[['study_hours']]
y = df['marks']

model = LinearRegression()
model.fit(X,y)

prediction = model.predict([[6]])

print("Predicted marks for 6 hours study:",prediction[0])

plt.scatter(X,y)
plt.plot(X,model.predict(X))
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Student Marks Prediction")
plt.show()
