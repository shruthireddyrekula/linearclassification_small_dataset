from sklearn import tree
features = [[150,0],[170,0],[130,1],[120,1]]
labels = [1,1,0,0]
clf = Tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
prediction = clf.predict([150,0])
print(prediction)
