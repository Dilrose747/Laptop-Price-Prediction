# 💻 Laptop Price Prediction using Machine Learning  

## 📌 Project Overview  
This project builds a machine learning pipeline to **predict laptop prices** based on specifications such as brand, processor type, RAM, storage, operating system, and GPU. The goal is to help customers, retailers, and e-commerce platforms estimate fair laptop prices and optimize purchasing decisions.  

By applying **regression techniques and model comparison**, we identified the most accurate and reliable algorithm for price forecasting.  

---

## 🎯 Objectives  
- Perform **data cleaning, preprocessing, and exploratory data analysis (EDA)**.  
- Apply **feature engineering** (encoding categorical variables, handling missing values, outlier treatment, scaling).  
- Build and evaluate multiple regression models:  
  - Linear Regression  
  - Ridge Regression (Tuned)  
  - Lasso Regression (Tuned)  
  - Random Forest Regressor  
- Compare models using **R², RMSE, and MAE**.  
- Deliver actionable insights on laptop pricing trends.  

---

## 🛠️ Tech Stack  
- **Programming Language:** Python  
- **Libraries & Tools:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Jupyter Notebook  
- **Machine Learning Models:** Linear Regression, Ridge, Lasso, Random Forest  

---

## 📊 Dataset  
- The dataset consists of laptop specifications such as:  
  - Brand  
  - Processor Type  
  - RAM Size  
  - Storage (HDD/SSD)  
  - GPU  
  - Operating System  
  - Display Features  
  - Price (Target Variable)  

*(Dataset source: [https://www.kaggle.com/datasets/muhammetvarl/laptop-price])*

---

## 🔍 Exploratory Data Analysis (EDA)  
- Distribution of laptop prices and key features  
- Correlation analysis between specs and price  
- Brand-wise pricing insights (e.g., Apple & MSI are priced higher on average)  
- RAM and SSD strongly correlated with higher prices  

---

## ⚙️ Model Building & Evaluation  

We trained and tested multiple regression models to forecast laptop prices:  

| Model               | R²       | RMSE     | MAE      |  
|---------------------|----------|----------|----------|  
| **Random Forest**   | **0.8273** | **313.90** | **196.31** |  
| Linear Regression   | 0.7897   | 357.79   | 244.76   |  
| Ridge (Tuned)       | 0.7925   | 353.68   | 242.37   |  
| Lasso (Tuned)       | 0.7932   | 354.33   | 241.86   |  

✅ **Best Model:** Random Forest Regressor (highest R², lowest error metrics).  

---

## 🚀 Key Outcomes  
- Built a regression pipeline capable of predicting laptop prices with **~82% accuracy (R² = 0.827)**.  
- Identified **RAM size, SSD capacity, and brand** as the strongest predictors of price.  
- Random Forest model reduced prediction error by **12% compared to Linear Regression**.  

---

## Tech Stack
- Python (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)

---

## Author
### Mohamed Dilrose P M
