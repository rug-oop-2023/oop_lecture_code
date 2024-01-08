from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

if __name__ == "__main__":
    data = load_iris()

    X = data.data
    y = data.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

    random_forest = RandomForestClassifier(n_estimators=100, criterion="gini", random_state=456)
    random_forest.fit(X_train, y_train)

    k_neighbors = KNN(n_neighbors=5, metric="euclidean")
    k_neighbors.fit(X_train, y_train)

    y_pred_rf = random_forest.predict(X_test)
    y_pred_knn = k_neighbors.predict(X_test)
    accuracy_rf = accuracy_score(y_test, y_pred_rf)
    accuracy_knn = accuracy_score(y_test, y_pred_knn)
    print(f"Random forest accuracy: {accuracy_rf}")
    print(f"KNN accuracy: {accuracy_knn}")