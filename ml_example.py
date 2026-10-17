#!/usr/bin/env python3
import numpy as np
from sklearn.linear_model import LinearRegression


def run_machine_learning():
    # 1. Feature matrix (X) and target values (y) following y = 2x
    X = np.array([[1], [2], [3], [4]])
    y = np.array([2, 4, 6, 8])

    # 2. Instantiate and train Linear Regression model
    model = LinearRegression()
    model.fit(X, y)

    # 3. Test prediction for input x = 5
    test_input = np.array([[5]])
    prediction = model.predict(test_input)

    print("--- Simple Machine Learning Prediction ---")
    print(f"Input: {test_input[0][0]}")
    print(f"Predicted Output: {prediction[0]:.1f} (Expected: 10.0)")


if __name__ == "__main__":
    run_machine_learning()
