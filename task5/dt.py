import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv('drug200.csv')

# Features & target
X = data.drop('Drug', axis=1)
y = data['Drug']

# Encode categorical columns
X['Sex'] = LabelEncoder().fit_transform(X['Sex'])
X['BP'] = LabelEncoder().fit_transform(X['BP'])
X['Cholesterol'] = LabelEncoder().fit_transform(X['Cholesterol'])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train model
model = DecisionTreeClassifier(
    criterion='entropy',
    max_depth=4,
    random_state=42
)
model.fit(X_train, y_train)

print("Accuracy:", accuracy_score(y_test, model.predict(X_test)))

plt.figure(figsize=(30, 18))     # VERY large canvas
plot_tree(
    model,
    feature_names=X.columns,
    class_names=model.classes_,
    filled=True,
    rounded=True,
    fontsize=8,                  # smaller text = less overlap
    max_depth=4                  # limit depth ONLY for plotting
)
plt.tight_layout()
plt.show()
