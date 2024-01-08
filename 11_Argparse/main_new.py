import argparse

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train a model on the Iris dataset.")
    parser.add_argument("--test_size", type=float, default=0.2, help="Fraction of data to use for testing.")
    parser.add_argument("--split_seed", type=int, default=123, help="Random state to use for train/test split.")
    parser.add_argument("--forest_ntree", type=int, default=100, help="Number of trees to use for random forest.")
    parser.add_argument("--forest_seed", type=int, default=456, help="Random state to use for random forest.")
    parser.add_argument("--forest_criterion", type=str, default="gini", choices=["gini", "entropy"], help="Criterion to use for random forest.")
    parser.add_argument("--knn_neighbors", type=int, default=5, help="Number of neighbors to use for KNN.")
    parser.add_argument("--knn_metric", type=str, default="euclidean", choices=["euclidean", "manhattan"], help="Distance metric to use for KNN.")
    parser.add_argument("--verbose", action="store_true", default=False, help="Show verbose output.")

    args = parser.parse_args()
    check_args(args)
    return args

def check_args(args) -> None:
    if args.test_size < 0 or args.test_size > 1:
        raise ValueError(f"Invalid test size: {args.test_size} (expected between 0.0 and 1.0).")
    if args.knn_neighbors < 1:
        raise ValueError(f"Invalid number of neighbors: {args.knn_neighbors} (expected at least 1).")
    

if __name__ == "__main__":
    args = parse_args()


    data = load_iris()

    verbosity_level = 2 * args.verbose

    X = data.data
    y = data.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=args.test_size, random_state=args.split_seed)

    random_forest = RandomForestClassifier(n_estimators=args.forest_ntree, criterion=args.forest_criterion, random_state=args.forest_seed, verbose=verbosity_level)
    random_forest.fit(X_train, y_train)

    k_neighbors = KNN(n_neighbors=args.knn_neighbors, metric=args.knn_metric)
    k_neighbors.fit(X_train, y_train)
    
    y_pred_rf = random_forest.predict(X_test)
    y_pred_knn = k_neighbors.predict(X_test)
    accuracy_rf = accuracy_score(y_test, y_pred_rf)
    accuracy_knn = accuracy_score(y_test, y_pred_knn)
    print(f"Random forest accuracy: {accuracy_rf}")
    print(f"KNN accuracy: {accuracy_knn}")