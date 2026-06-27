#!/bin/bash
# ============================================================
# GitHub Repository Setup Script
# NZ Wellbeing Forecasting Project
# ============================================================
# Prerequisites:
#   - Git installed
#   - GitHub CLI (gh) installed OR personal access token
#   - Python 3.8+, Node.js 16+
# ============================================================

set -e

REPO_NAME="nz-wellbeing-forecasting"
GITHUB_USER="YOUR_GITHUB_USERNAME"  # ← Replace with your username

echo "🚀 Setting up NZ Wellbeing Forecasting GitHub repo..."

# 1. Initialize git
git init
git add .
git commit -m "Initial commit: NZ Wellbeing Forecasting — 5-model comparison

- Linear Regression, XGBoost (GBM), LSTM, ANN, ARIMA(1,1,1)
- 10 wellbeing indicators from Stats NZ NZGSS 2014-2018
- 2020 forecasts with MAE/RMSE/R²/MAPE evaluation
- 10-slide PowerPoint presentation
- Full visualizations and metrics CSVs"

# 2. Create GitHub repo (using gh CLI)
# Option A: GitHub CLI
gh repo create $REPO_NAME --public --description "NZ Wellbeing Time-Series Forecasting: Linear Regression vs XGBoost vs LSTM vs ANN vs ARIMA on Stats NZ data"

# Option B: Using curl + personal token (uncomment if no gh CLI)
# TOKEN="your_github_pat_here"
# curl -H "Authorization: token $TOKEN" https://api.github.com/user/repos \
#      -d "{\"name\":\"$REPO_NAME\",\"description\":\"NZ Wellbeing Forecasting\",\"public\":true}"

# 3. Push
git branch -M main
git remote add origin https://github.com/$GITHUB_USER/$REPO_NAME.git
git push -u origin main

echo ""
echo "✅ Done! Your repo is live at:"
echo "   https://github.com/$GITHUB_USER/$REPO_NAME"
