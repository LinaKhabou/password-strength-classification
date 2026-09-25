# 🔐 Password Strength Classification

## 📌 Overview

This project is a **Machine Learning classification project** that predicts the strength of a password based on its character patterns.

The model classifies passwords into three categories:

* 🔴 **Weak**
* 🟠 **Medium**
* 🟢 **Strong**

The project uses **Natural Language Processing (NLP)** techniques, specifically **character-level TF-IDF with character n-grams**, to transform passwords into numerical features that can be used by Machine Learning models.

A **Streamlit web application** was also developed to provide real-time password strength predictions.

---

## 🎯 Objective

The goal of this project is to build a Machine Learning model capable of classifying passwords into different strength levels.

The project follows a complete Machine Learning workflow:

* Data understanding and cleaning
* Exploratory Data Analysis (EDA)
* Train/test splitting
* Character-level feature extraction
* TF-IDF vectorization
* Model training
* Model comparison
* Model evaluation
* Model serialization
* Streamlit deployment

---

## 🔄 Project Pipeline

```text
Password Dataset
       ↓
Data Cleaning
       ↓
Exploratory Data Analysis
       ↓
Train / Test Split
       ↓
Character-level TF-IDF
       ↓
Logistic Regression & Linear SVM
       ↓
Model Evaluation
       ↓
Best Model Selection
       ↓
Streamlit Application
```

---

## 📊 Dataset

The dataset contains passwords and their corresponding strength labels.

| Column     | Description                |
| ---------- | -------------------------- |
| `password` | Password to classify       |
| `strength` | Password strength category |

The target variable contains three classes:

* **Weak**
* **Medium**
* **Strong**

Missing values were removed before training.


## 🧠 NLP Approach

Passwords are not traditional natural language, but they can still be represented as **sequences of characters**.

For this project, a **character-level TF-IDF vectorizer** was used:

```python
TfidfVectorizer(
    analyzer="char",
    ngram_range=(1,2)
)
```

This means that the vectorizer analyzes individual characters and sequences of up to two consecutive characters.

For example, a password such as:

```text
abc123
```

can be represented using character patterns such as:

```text
a
b
c
1
2
3
ab
bc
c1
12
23
```

These character patterns are transformed into numerical TF-IDF features and then provided to the Machine Learning models.

---

## 🤖 Machine Learning Models

Two classification algorithms were trained and compared:

### 1. Logistic Regression

Logistic Regression was used as one of the baseline classification models.

### 2. Linear SVM

A **Linear Support Vector Machine (SVM)** was also trained to determine whether it could provide better classification performance.

Both models used:

```python
class_weight="balanced"
```

to take class distribution into account during training.

---

## 📈 Model Evaluation

The models were evaluated on a separate test set using:

* **Accuracy**
* **Precision**
* **Recall**
* **F1-score**
* **Classification Report**

The models were compared based on their performance on the test set.

### Model Comparison

| Model               |   Accuracy |
| ------------------- | ---------: |
| Logistic Regression | **87.30%** |
| Linear SVM          | **87.48%** |

**Linear SVM achieved the best accuracy (87.48%) and was selected as the final model for the Streamlit application.**

Although the difference between the two models is small, Linear SVM provided the best overall accuracy on the test set.

---

## 💾 Model Saving

The final Linear SVM model was saved using Pickle:

```text
models/model.pkl
```

The fitted TF-IDF vectorizer was also saved:

```text
models/tfidf_vectorizer.pkl
```

Saving both objects allows the Streamlit application to use the same preprocessing and trained model without retraining them every time.

---

## 🖥️ Streamlit Application

A Streamlit application was developed to allow users to enter a password and receive a real-time prediction.

The application follows this process:

```text
User enters password
        ↓
Saved TF-IDF Vectorizer
        ↓
Saved Linear SVM Model
        ↓
Password strength prediction
        ↓
Weak / Medium / Strong
```

---

## 🛠️ Technologies

* **Python**
* **Pandas**
* **Matplotlib**
* **Scikit-learn**
* **TF-IDF**
* **Character n-grams**
* **Logistic Regression**
* **Linear SVM**
* **Pickle**
* **Streamlit**


## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/password-strength-classification.git
cd password-strength-classification
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

