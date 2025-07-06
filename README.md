# Student Exam Score Predictor

This Streamlit web app predicts a student's **math score** based on their reading and writing scores, and personal background factors like gender, ethnicity, lunch type, parental education, and test preparation course.

It is built using a machine learning model trained on the [Kaggle "Students Performance in Exams" dataset](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams).

---

## Objective

To understand how student performance (especially math scores) is influenced by various factors such as:
- Gender
- Ethnicity
- Parental level of education
- Lunch type (standard or free/reduced)
- Test preparation course
- Reading score
- Writing score

---

##  How It Works

1. The user enters details like gender, parental education, reading/writing scores, etc.
2. The input is passed through a preprocessing pipeline.
3. A trained ML model (selected using GridSearchCV) predicts the math score.

---

## Try the App

👉 [Click here to use the app](https://student-score-predictor-vzbnnfikgsazmzk8cyhwcq.streamlit.app)

---

## Dataset Used

- Source: [Kaggle - Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- Features:
  - Categorical: `gender`, `race/ethnicity`, `parental level of education`, `lunch`, `test preparation course`
  - Numerical: `reading score`, `writing score`
- Target: `math score`

---

## Model Training

- Model selection and hyperparameter tuning is done using `GridSearchCV`.
- `model_trainer.py` script selects the best model based on R² score.
- Best model and preprocessor are saved to the `artifacts/` directory using `pickle`.

---

## 📁 Folder Structure

```
Student-Performance-Predictor/
├── app.py                     # Main Streamlit app; takes user input and displays predicted math score
├── setup.py                   # Setup file to package the project as a Python module
├── notebook/                  # Jupyter notebooks for data exploration and model development
│   ├── EDA.ipynb              # Exploratory Data Analysis notebook (visualizations, insights)
│   └── Model_Training.ipynb   # Notebook for model selection, training, and evaluation
├── requirements.txt           # List of Python dependencies needed to run the project
├── artifacts/                 # Stores all generated artifacts during training and deployment
│   ├── data.csv               # Raw dataset from Kaggle
│   ├── train.csv              # Training dataset split
│   ├── test.csv               # Testing dataset split
│   ├── model.pkl              # Final trained machine learning model (pickle file)
│   └── preprocessor.pkl       # Fitted preprocessing pipeline (e.g., encoders, scalers)
├── src/                       # All source code is organized here
│   ├── __init__.py            # Makes src a Python package
│   ├── components/            # Contains core ML pipeline building blocks
│   │   ├── __init__.py        
│   │   ├── data_ingestion.py          # Code to load and split data into train/test sets
│   │   ├── data_transformation.py     # Feature engineering and preprocessing logic
│   │   └── model_trainer.py           # Trains models using GridSearchCV and selects best one
│   ├── pipeline/                      # Logic used at inference time (Streamlit and CLI prediction)
│   │   ├── __init__.py
│   │   ├── prediction_pipeline.py     # Loads model and preprocessor, performs prediction
│   │   └── train_pipeline.py          # Optional pipeline wrapper to trigger full training workflow
│   ├── utils.py                       # Common utility functions (e.g., save/load pickle, evaluation metrics)
│   ├── exception.py           # Custom exception class with traceback support
│   └── logger.py              # Logging configuration for all project modules
├── .gitignore                 # Git ignore rules (e.g., to exclude logs, __pycache__, .pkl files)
└── README.md                  # Project overview, usage instructions, and deployment info
```
## How to Run Locally

Follow these steps to run the project on your local machine:

###  1. Clone the repository

```bash
git clone https://github.com/your-username/Student-Performance-Predictor.git
cd Student-Performance-Predictor
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Launch the Streamlit app
```bash
streamlit run app.py
```
