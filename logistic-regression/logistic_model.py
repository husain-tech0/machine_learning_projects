from sklearn.linear_model import LogisticRegression

X = [[10],[20],[30],[80]]
y = [0,0,1,0]

model = LogisticRegression()
model.fit(X,y)

print(model.predict([[50]]))
