from sklearn import tree
features = [[0.9],[1.0],[1.1],[1.2],[1.21],[0.1],[0.4],[0.2],[0.3],[0.45]]
labels = [1,1,1,1,1,0,0,0,0,0]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
prediction = clf.predict([[0.51]])
