````markdown
# 🧬 Frameworks_Assignment — CORD-19 Data Analysis and Streamlit App

## 📖 Project Overview
This project explores the **CORD-19 COVID-19 research dataset**, focusing on metadata of published papers.  
It demonstrates essential **data analysis, visualization, and web app development skills** using Python frameworks.

---

## 🎯 Objectives
By completing this assignment, I practiced:
- Loading and exploring real-world data with **pandas**
- Performing **data cleaning**
- Creating meaningful **visualizations** with Matplotlib and Seaborn
- Building a simple **Streamlit web app** for data interaction
- Presenting insights effectively

---

## 🧰 Tools and Libraries
- Python 3.13
- pandas  
- matplotlib  
- seaborn  
- streamlit  
- Jupyter Notebook

To install all dependencies:
```bash
pip install pandas matplotlib seaborn streamlit
````

---

## 📊 Data Source

Dataset: [CORD-19 Research Challenge (Kaggle)](https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge)
File used: `metadata_sample.csv` (sampled from `metadata.csv`)

---

## 🧮 Project Structure

```
Frameworks_Assignment/
│
├── analysis.ipynb          # Jupyter notebook with full analysis
├── metadata_sample.csv     # Sample of the dataset used
├── app.py                  # Streamlit application
└── README.md               # Project documentation
```

---

## 🧠 Key Steps

### 1️⃣ Data Loading and Exploration

* Loaded dataset with pandas
* Checked shape, info, and missing values

### 2️⃣ Data Cleaning

* Dropped empty titles and publication dates
* Extracted publication year from `publish_time`

### 3️⃣ Visualization

* Publications by year
* Top journals by publication count

### 4️⃣ Streamlit App

Interactive web app built with:

```bash
streamlit run app.py
```

Features:

* Displays data sample
* Year range filter (slider)
* Two visualizations:

  * Publications by Year
  * Top 10 Journals

---

## 📈 Insights

* Publication volume increased significantly in 2020 due to COVID-19 research.
* A few journals (like *medRxiv* and *bioRxiv*) dominated early pandemic publications.

---

## 🪄 Reflection

This assignment improved my understanding of:

* Data cleaning and visualization in Python
* Streamlit app creation and layout
* GitHub project structure and documentation

---

## 👨‍💻 Author

**Name:** [ADEWUNMI LOLADE]
**GitHub:** [(https://github.com/adecares-Dev) ]
**Date:** October 2025

```

---
