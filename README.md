# Simple Machine Learning Example: Linear Regression

This project demonstrates the simplest example of Machine Learning using Linear Regression to learn the mathematical relationship $y = 2x$.

## How the Code Works
1. **Dataset Creation:** We define a small dataset of numerical inputs (`X = [[1], [2], [3], [4]]`) and target outputs (`y = [2, 4, 6, 8]`).
2. **Model Initialization:** We instantiate a `LinearRegression` model using `scikit-learn`.
3. **Training (`.fit()`):** The algorithm processes the input-output pairs to calculate the mathematical slope and intercept.
4. **Prediction (`.predict()`):** We feed an unseen test input (`x = 5`) into the model to confirm that it accurately predicts `10.0`.

## Setup and Running Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
