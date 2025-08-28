import autosklearn.classification
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main():
    # Загрузка данных
    X, y = load_iris(return_X_y=True)

    # Разделение на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    # Инициализация AutoSklearnClassifier
    automl = autosklearn.classification.AutoSklearnClassifier(
        time_left_for_this_task=60,
        per_run_time_limit=30,
        n_jobs=-1,
        seed=42
    )

    # Обучение модели
    automl.fit(X_train, y_train)

    # Предсказание и оценка
    y_pred = automl.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))

if __name__ == "__main__":
    main()