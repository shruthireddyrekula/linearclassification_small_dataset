from sklearn import tree
features = [[150,0],[170,0],[130,1],[120,1]] #0 = bumpy 1 = smooth
labels = [1,1,0,0] #1 = orange 0 =  apple
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
prediction = clf.predict([[150,0]])
print(prediction)
