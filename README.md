# Iris Dataset Prediction Application (Django)

## Overview

This Django-based web application predicts the species of iris flowers using the famous Iris dataset. The application employs a machine learning model to classify iris flowers based on their sepal and petal dimensions.

## Features

- **Iris Species Prediction**: Enter sepal and petal dimensions to predict the species (Setosa, Versicolor, or Virginica).
- **Interactive Web Interface**: User-friendly forms for input and result display.
- **Pretrained Model**: A machine learning model trained on the Iris dataset for high accuracy.
- 
## Requirements

### Software Requirements
- **Python**: 3.8+
- **Django**: 3.2+
- **scikit-learn**: For machine learning model training and prediction
- **Django REST Framework**: For API support

### Dataset
- **Iris Dataset**: A built-in dataset from scikit-learn.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/AllaUjwalSai/iris-prediction-app.git
   cd iris-prediction-app
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Load Pretrained Model**:
   - Ensure the pretrained model (`iris_model.pkl`) is in the project directory.

6. **Start the Server**:
   ```bash
   python manage.py runserver
   ```

## Usage

1. **Access the Web Application**:
   - Open a web browser and navigate to `http://127.0.0.1:8000`.

2. **Make Predictions**:
   - Enter the sepal length, sepal width, petal length, and petal width.
   - Click "Predict" to view the species prediction.

3. **Use the API**:
   - Send a POST request to `/api/predict/` with the following JSON payload:
     ```json
     {
       "sepal_length": 5.1,
       "sepal_width": 3.5,
       "petal_length": 1.4,
       "petal_width": 0.2
     }
     ```
   - The response will include the predicted species.

## Project Structure

```
project_root/
├── iris_app/                              # Django app for prediction
│   ├── migrations/                        # Database migrations
│   ├── models.py                          # Database models
│   ├── serializers.py                     # API serializers
│   ├── templates/                         # HTML templates
│   ├── urls.py                            # URL routing
│   └── views.py                           # View logic
├── static/                                # Static files
├── templates/                             # Project-level templates
├── manage.py                              # Django management script
├── requirements.txt                       # Python dependencies
├── iris_model.pkl                         # Pretrained ML model
└── README.md                              # Project documentation
```

## Key Components

- **scikit-learn**: Trained the machine learning model using the Iris dataset.
- **Django REST Framework**: Exposes an API endpoint for predictions.
- **HTML Templates**: Provides an interactive user interface.

## Contributing

1. **Fork the Repository**.
2. **Create a Feature Branch**:
   ```bash
   git checkout -b feature-name
   ```
3. **Commit Changes**:
   ```bash
   git commit -m 'Add feature'
   ```
4. **Push to the Branch**:
   ```bash
   git push origin feature-name
   ```
5. **Open a Pull Request**.


## Acknowledgments

- Scikit-learn for the Iris dataset and machine learning tools.
- Django and Django REST Framework for simplifying web development.

## Contact

For questions or support, contact [Ujwal] at [ujwalsai16@gmail.com].

