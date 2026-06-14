{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "ae9dc44b-b334-4e14-b09b-34f4a8c96e62",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Years: 14\n",
      "  Linear Regression: $153441.74\n",
      "  Polynomial Regression (Deg 3): $138926.10\n",
      "Years: 14.5\n",
      "  Linear Regression: $157973.48\n",
      "  Polynomial Regression (Deg 3): $138763.90\n",
      "Years: 15\n",
      "  Linear Regression: $162505.22\n",
      "  Polynomial Regression (Deg 3): $137905.07\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/anaconda3/lib/python3.12/site-packages/sklearn/utils/validation.py:2691: UserWarning: X does not have valid feature names, but PolynomialFeatures was fitted with feature names\n",
      "  warnings.warn(\n",
      "/opt/anaconda3/lib/python3.12/site-packages/sklearn/utils/validation.py:2691: UserWarning: X does not have valid feature names, but LinearRegression was fitted with feature names\n",
      "  warnings.warn(\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.preprocessing import PolynomialFeatures\n",
    "\n",
    "# Load data\n",
    "df = pd.read_csv('/Users/earltavera/Desktop/MSE803/Week 10/salary-dataset.csv')\n",
    "if 'Unnamed: 0' in df.columns:\n",
    "    df = df.drop(columns=['Unnamed: 0'])\n",
    "\n",
    "X = df[['YearsExperience']]\n",
    "y = df['Salary']\n",
    "\n",
    "# Fit full models for prediction to use maximum data\n",
    "lr_model = LinearRegression()\n",
    "lr_model.fit(X, y)\n",
    "\n",
    "poly_features = PolynomialFeatures(degree=3)\n",
    "X_poly = poly_features.fit_transform(X)\n",
    "poly_model = LinearRegression()\n",
    "poly_model.fit(X_poly, y)\n",
    "\n",
    "# Prediction points\n",
    "X_new = np.array([[14], [14.5], [15]])\n",
    "X_new_poly = poly_features.transform(X_new)\n",
    "\n",
    "preds_lr = lr_model.predict(X_new)\n",
    "preds_poly = poly_model.predict(X_new_poly)\n",
    "\n",
    "for exp, p_lr, p_poly in zip([14, 14.5, 15], preds_lr, preds_poly):\n",
    "    print(f\"Years: {exp}\")\n",
    "    print(f\"  Linear Regression: ${p_lr:.2f}\")\n",
    "    print(f\"  Polynomial Regression (Deg 3): ${p_poly:.2f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6805d104-366a-4d24-99c2-31232341f798",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Years: 14 -> Polynomial Regression (Deg 2): $149313.84\n",
      "Years: 14.5 -> Polynomial Regression (Deg 2): $153002.59\n",
      "Years: 15 -> Polynomial Regression (Deg 2): $156632.76\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/opt/anaconda3/lib/python3.12/site-packages/sklearn/utils/validation.py:2691: UserWarning: X does not have valid feature names, but PolynomialFeatures was fitted with feature names\n",
      "  warnings.warn(\n"
     ]
    }
   ],
   "source": [
    "poly_features_2 = PolynomialFeatures(degree=2)\n",
    "X_poly_2 = poly_features_2.fit_transform(X)\n",
    "poly_model_2 = LinearRegression()\n",
    "poly_model_2.fit(X_poly_2, y)\n",
    "\n",
    "X_new_poly_2 = poly_features_2.transform(X_new)\n",
    "preds_poly_2 = poly_model_2.predict(X_new_poly_2)\n",
    "\n",
    "for exp, p_poly2 in zip([14, 14.5, 15], preds_poly_2):\n",
    "    print(f\"Years: {exp} -> Polynomial Regression (Deg 2): ${p_poly2:.2f}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "ffa58fbf-040f-4199-8c77-d4df6dbea301",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Years      | Linear Reg     | Poly Reg (Deg 2)  | Poly Reg (Deg 3)  \n",
      "----------------------------------------------------------------------\n",
      "14.0       | $153,441.74    | $149,313.84       | $138,926.10\n",
      "14.5       | $157,973.48    | $153,002.59       | $138,763.90\n",
      "15.0       | $162,505.22    | $156,632.76       | $137,905.07\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.preprocessing import PolynomialFeatures\n",
    "\n",
    "# 1. Load the dataset\n",
    "df = pd.read_csv('/Users/earltavera/Desktop/MSE803/Week 10/salary-dataset.csv')\n",
    "if 'Unnamed: 0' in df.columns:\n",
    "    df = df.drop(columns=['Unnamed: 0'])\n",
    "\n",
    "X = df[['YearsExperience']]\n",
    "y = df['Salary']\n",
    "\n",
    "# 2. Fit the Linear Regression Model\n",
    "lr_model = LinearRegression()\n",
    "lr_model.fit(X, y)\n",
    "\n",
    "# 3. Fit the Polynomial Regression Model (Degree 2)\n",
    "poly_features_d2 = PolynomialFeatures(degree=2)\n",
    "X_poly_d2 = poly_features_d2.fit_transform(X)\n",
    "poly_model_d2 = LinearRegression()\n",
    "poly_model_d2.fit(X_poly_d2, y)\n",
    "\n",
    "# 4. Fit the Polynomial Regression Model (Degree 3)\n",
    "poly_features_d3 = PolynomialFeatures(degree=3)\n",
    "X_poly_d3 = poly_features_d3.fit_transform(X)\n",
    "poly_model_d3 = LinearRegression()\n",
    "poly_model_d3.fit(X_poly_d3, y)\n",
    "\n",
    "# 5. Define target experience levels as a DataFrame (fixes UserWarning)\n",
    "X_new = pd.DataFrame([[14.0], [14.5], [15.0]], columns=['YearsExperience'])\n",
    "\n",
    "# Transform features for polynomial models\n",
    "X_new_poly_d2 = poly_features_d2.transform(X_new)\n",
    "X_new_poly_d3 = poly_features_d3.transform(X_new)\n",
    "\n",
    "# 6. Run predictions\n",
    "preds_lr = lr_model.predict(X_new)\n",
    "preds_poly_d2 = poly_model_d2.predict(X_new_poly_d2)\n",
    "preds_poly_d3 = poly_model_d3.predict(X_new_poly_d3)\n",
    "\n",
    "# 7. Safely display results without format conflicts\n",
    "print(f\"{'Years':<10} | {'Linear Reg':<14} | {'Poly Reg (Deg 2)':<17} | {'Poly Reg (Deg 3)':<18}\")\n",
    "print(\"-\" * 70)\n",
    "for i, exp in enumerate([14.0, 14.5, 15.0]):\n",
    "    # Format to currency strings first\n",
    "    str_lr = f\"${preds_lr[i]:,.2f}\"\n",
    "    str_poly_d2 = f\"${preds_poly_d2[i]:,.2f}\"\n",
    "    str_poly_d3 = f\"${preds_poly_d3[i]:,.2f}\"\n",
    "    \n",
    "    # Pad and print strings safely (fixes ValueError)\n",
    "    print(f\"{exp:<10} | {str_lr:<14} | {str_poly_d2:<17} | {str_poly_d3}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0cfec001-251f-4358-aa8b-5ab762954bf8",
   "metadata": {},
   "outputs": [],
   "source": [
    "When you train a model, you want it to capture the underlying trend of the data rather than the random noise.Degree 1 (Linear): Assumes a strict straight line. It is highly stable but might be too simple (underfitting) if salary growth slows down over time.Degree 2 (Quadratic): Introduces a single bend (a parabola). It allows the model to capture \"diminishing returns\"—the very realistic trend where your salary grows quickly early in your career and begins to level off later.Degree 3 (Cubic): Introduces two bends. While it might match the training data slightly closer (yielding a lower error during testing), it can behave erratically the moment you try to predict values outside the original dataset range ($X > 13$ years)."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
