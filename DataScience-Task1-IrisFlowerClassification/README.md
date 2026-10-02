# 🌸 Iris Flower Classification

## Oasis Infobyte — Data Science Task 1

This project develops a machine learning classification model to predict the species of an Iris flower based on its sepal and petal measurements.

The project classifies Iris flowers into three species:

* Setosa
* Versicolor
* Virginica

---

## 🎯 Objective

The objective of this project is to build and evaluate machine learning classification models using the Iris dataset and select the best-performing model based on evaluation and cross-validation results.

---

## 📊 Dataset

The Iris dataset is directly available through `scikit-learn`, so no external dataset download is required.

```python
from sklearn.datasets import load_iris

iris = load_iris()
```

### Dataset Details

* **Samples:** 150
* **Features:** 4
* **Classes:** 3
* **Missing Values:** None

### Features

1. Sepal Length
2. Sepal Width
3. Petal Length
4. Petal Width

### Target Classes

* Setosa
* Versicolor
* Virginica

---

## 🔍 Exploratory Data Analysis

The following EDA steps were performed:

* Dataset shape inspection
* Data type checking
* Missing value checking
* Descriptive statistics
* Feature distribution analysis
* Pairplot visualization
* Box plots
* Feature relationship analysis

The analysis showed that **petal length and petal width provide strong separation between the Iris species**.

---

## 🧠 Feature Selection

All four available features were retained for model training.

Petal length and petal width showed stronger class discrimination, while sepal measurements also provided useful information for classification.

---

## 🤖 Machine Learning Models

The following classification algorithms were trained and evaluated:

1. K-Nearest Neighbors (KNN)
2. Logistic Regression
3. Decision Tree
4. Random Forest

---

## ⚙️ Model Training

The dataset was divided into training and testing sets using an 80/20 split.

```python
train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)
```

Five-fold cross-validation and GridSearchCV were used for hyperparameter tuning.

The macro F1-score was used as the primary tuning metric because this is a multiclass classification problem.

---

## 📈 Model Evaluation

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix
* ROC-AUC

### Test Set Results

| Model               | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
| ------------------- | -------: | --------: | -----: | -------: | ------: |
| KNN                 |   1.0000 |    1.0000 | 1.0000 |   1.0000 |  1.0000 |
| Logistic Regression |   1.0000 |    1.0000 | 1.0000 |   1.0000 |  1.0000 |
| Decision Tree       |   0.9333 |    0.9333 | 0.9333 |   0.9333 |  0.9733 |
| Random Forest       |   0.9667 |    0.9697 | 0.9667 |   0.9666 |  0.9867 |

---

## 🔄 Cross-Validation Results

| Model               | Mean CV F1-Score | Standard Deviation |
| ------------------- | ---------------: | -----------------: |
| KNN                 |          0.97497 |            0.03335 |
| Logistic Regression |          0.96634 |            0.03162 |
| Random Forest       |          0.95817 |            0.00000 |
| Decision Tree       |          0.94130 |            0.02066 |

---

## 🏆 Final Model

Based on the observed cross-validation and test-set results, **K-Nearest Neighbors (KNN)** was selected as the final model.

### Best KNN Parameters

```text
Number of Neighbors: 5
Distance Metric: Euclidean
Weights: Uniform
```

The KNN model achieved:

```text
Cross-Validation F1-Score: 0.97497
Test F1-Score: 1.00000
```

The test set contains only 30 samples, so the 100% test score should not be interpreted as proof of perfect real-world generalization.

---

## 💾 Saved Model

The final trained model is saved using Joblib:

```text
iris_flower_classification_knn_model.pkl
```

The saved model can be loaded without retraining:

```python
import joblib

model = joblib.load(
    "iris_flower_classification_knn_model.pkl"
)
```

---

## 🌐 Live Demo

A Gradio-based web application is provided for live prediction.

The application allows users to enter:

* Sepal Length
* Sepal Width
* Petal Length
* Petal Width

The application returns:

* Predicted Iris species
* Prediction probabilities
* Input feature summary

The application is designed for deployment using **Hugging Face Spaces**.

---

## 📁 Project Structure

```text
DataScience-Task1-IrisFlowerClassification/
│
├── Iris_Flower_Classification.ipynb
├── app.py
├── iris_flower_classification_knn_model.pkl
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── eda.png
    ├── model_comparison.png
    ├── confusion_matrix.png
    └── live_demo.png
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Jupyter Notebook
* Gradio
* Hugging Face Spaces

---

## ▶️ Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/OIBSIP.git
```

### 2. Navigate to the project

```bash
cd OIBSIP/DataScience-Task1-IrisFlowerClassification
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Gradio application

```bash
python app.py
```

The Gradio application will provide a local URL in the terminal.

---

## 📌 Oasis Infobyte Internship

**Track:** Data Science

**Task:** Task 1 — Iris Flower Classification

This project follows the required Oasis Infobyte Data Science Task 1 workflow, including data loading, EDA, visualization, feature selection discussion, train-test splitting, multiple classifiers, model evaluation, and final model selection.

---

## 👨‍💻 Author

**Madesh P**

B.Tech Artificial Intelligence & Data Science
CARE College of Engineering
Batch: 2023–2027
