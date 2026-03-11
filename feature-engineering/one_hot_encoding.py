from sklearn.preprocessing import OneHotEncoder

colors = [["black"], ["purple"], ["pink"]]

encoder = OneHotEncoder()

result = encoder.fit_transform(colors)

print(result.toarray())
