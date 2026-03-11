from sklearn.model_selection import KFold

data = [10,20,30,40,50]

kf = KFold(n_splits=5)

for train, test in kf.split(data):
    print("Train:", [data[i] for i in train])
    print("Test:", [data[i] for i in test])
    print()
