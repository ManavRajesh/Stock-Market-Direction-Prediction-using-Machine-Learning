from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression

def get_models():
    return {
        "Linear SVM": Pipeline([
            ('scaler', StandardScaler()),
            ('model', LinearSVC())
        ]),
        "Logistic": Pipeline([
            ('scaler', StandardScaler()),
            ('model', LogisticRegression(max_iter=1000))
        ])
    }
