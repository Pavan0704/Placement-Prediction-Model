import pandas as pd
import numpy as np

df = pd.read_csv('placement.csv')

df.head()

df = df.iloc[:,1:]

df.head()

import matplotlib.pyplot as plt
plt.scatter(df["cgpa"], df["iq"], c = df['placement'])

x = df.iloc[:,0:2]
y = df.iloc[:,-1]

Train and Test Split

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)

Scaling

from sklearn.preprocessing import StandardScaler
sc = StandardScaler() #created a scaler object
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

Training

from sklearn.linear_model import LogisticRegression
clf = LogisticRegression()
clf.fit(x_train, y_train)

Evaluation

y_pred = clf.predict(x_test) #x_test because it's the hidden test data of the students
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_pred))

Plotting of Decission Boundary

from mlxtend.plotting import plot_decision_regions
plot_decision_regions(x_train, y_train.values, clf=clf, legend =2)

Extracting the Model

import pickle
pickle.dump(clf, open('model.pkl', 'wb'))
