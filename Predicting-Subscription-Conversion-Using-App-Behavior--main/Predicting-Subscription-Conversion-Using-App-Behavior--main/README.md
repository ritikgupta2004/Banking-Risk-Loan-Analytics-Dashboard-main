# Predicting-Subscription-Conversion-Using-App-Behavior

# Problem Statement

Many companies in today’s marketplace have mobile apps that offer both free and paid versions. While users often start with the free version, companies want them to convert into paying subscribers (examples: _YouTube Premium, Spotify Premium, Pandora Premium_, etc.).

The challenge is that not every free user is likely to enroll. If the company spends marketing budget equally on all free users, they end up wasting money targeting people who would have subscribed anyway, or those who would never subscribe.

This project is about identifying which free users are _unlikely to convert into paid members_, so that marketing campaigns can be targeted towards the right audience, saving cost and improving conversion rates.

# Project Objective

I was tasked with analyzing user app behavior data collected during the _first 24 hours of app usage_.

The goal is to:

- Perform **Exploratory Data Analysis (EDA)** to understand user patterns.
- Engineer features from app usage (like types of screens visited, time difference between actions, etc.).
- Use this processed dataset to later build _classification models_ that can predict whether a user will enroll into the paid product.

By doing this, the fintech company can launch _targeted campaigns right after the free trial ends_ (since the free trial lasts 24 hours), increasing the chances of successful conversion.

# Dataset Description

The dataset is synthetic but realistic — distributions and patterns mimic real-world app usage in fintech.

It includes user behavior such as:

- Screens visited in the mobile app
- Timestamps for first open and enrollment
- Various app activity features

The dataset is _not clean by default_ and requires preprocessing before applying machine learning.

# What We Did (So Far)

### **1. Exploratory Data Analysis (EDA)**  
- Inspected dataset head and summary statistics  
- Cleaned timestamp data and extracted usage hours  
- Visualized feature distributions and correlations using Seaborn heatmaps  

### **2. Feature Engineering (Date/Time)**  
- Converted string columns into `datetime` format  
- Calculated time between `first_open` and `enrolled_date`  
- Marked users taking more than 48 hours to enroll as unlikely converters  

### **3. Feature Engineering (App Screens)**  
- Extracted top app screens and created binary features  
- Grouped remaining screens into an `OtherScreens` feature  

### **4. Funnel Creation**  
Grouped similar screens into behavioral funnels:  
- `SavingCount` → Savings-related screens  
- `CMCount` → Credit management screens  
- `CCCount` → Credit card screens  
- `LoansCount` → Loan-related screens  

### **5. Exported Processed Data**  
- Final cleaned and engineered dataset saved as **`new_appdata10.csv`** for modeling  

### **6. Model Development (Logistic Regression)**  
- Built and trained a **Logistic Regression classification model** to predict user enrollment  
- Applied **feature scaling** and used both **L1/L2 regularization** techniques  
- Evaluated model using **accuracy**, **precision**, **recall**, and **F1-score**  
- Performed **10-fold Cross Validation** to validate performance consistency  
- Conducted **Grid Search** for hyperparameter tuning (`C`, `penalty`)  
- Generated final predictions and combined them with user IDs for analysis  

# Tools and Libraries

- Python (data processing and ML experiments)
- Pandas, Numpy (data handling and manipulation)
- Matplotlib, Seaborn (data visualization)
- Dateutil (date formatting and parsing)

# Repository Structure

Dataset/
- appdata10.csv          # Original raw dataset
- top_screens.csv        # List of top app screens
- new_appdata10.csv          # Final cleaned and engineered dataset
- main.py           # Script for EDA and feature engineering
- model_logistic.py          # Logistic Regression model training and tuning script
- README.md                  # Project documentation (this file)



