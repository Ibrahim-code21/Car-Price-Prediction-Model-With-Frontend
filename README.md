# 🚗 Car Price Prediction Model with Frontend

A machine learning project that predicts car selling prices using Linear Regression and Random Forest algorithms, complete with an interactive Streamlit web interface.

## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Dataset](#dataset)
- [Model Performance](#model-performance)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [How It Works](#how-it-works)
- [Screenshots](#screenshots)-
- [Contributing](#contributing)


## 🎯 Overview

This project implements a comprehensive car price prediction system that helps users estimate the selling price of used cars based on various features like age, mileage, fuel type, transmission, and more. The system uses two machine learning algorithms and provides an intuitive web interface for easy predictions.

## ✨ Features

- **Dual Model Support**: Choose between Linear Regression and Random Forest models
- **Interactive Web Interface**: User-friendly Streamlit application
- **Real-time Predictions**: Instant price estimates based on car specifications
- **Depreciation Analysis**: Shows how much value the car has lost
- **Model Comparison**: Compare predictions from both algorithms
- **Input Validation**: Ensures data quality with proper ranges and constraints
- **Detailed Insights**: View complete input details in an expandable section

## 📊 Dataset

The project uses a dataset of 301 used cars with the following features:

- **Car_Name**: Model name of the car
- **Year**: Manufacturing year
- **Selling_Price**: Price at which car was sold (Target variable)
- **Present_Price**: Current showroom price of the model
- **Driven_kms**: Total kilometers driven
- **Fuel_Type**: Petrol, Diesel, or CNG
- **Selling_type**: Dealer or Individual
- **Transmission**: Manual or Automatic
- **Owner**: Number of previous owners (0, 1, or 3+)

### Dataset Statistics:
- **Total Records**: 301 cars
- **Price Range**: ₹0.10 - ₹35.00 Lakhs
- **Age Range**: 7 - 22 years
- **Mileage Range**: 500 - 500,000 km

## 📈 Model Performance

### Linear Regression
- **R² Score**: 84.89%
- **Training Speed**: Very Fast
- **Interpretability**: Excellent
- **Use Case**: Quick predictions with clear reasoning

### Random Forest (Recommended)
- **R² Score**: 95.82%
- **Mean Absolute Error**: ±0.64 Lakhs
- **Training Speed**: Fast
- **Use Case**: Maximum accuracy for price predictions

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Clone the Repository
```bash
git clone https://github.com/Ibrahim-code21/Car-Price-Prediction-Model-With-Frontend.git
cd Car-Price-Prediction-Model-With-Frontend
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

Required packages:
- streamlit
- pandas
- scikit-learn
- pickle

### Step 3: Verify Installation
```bash
python --version
streamlit --version
```

## 🚀 Usage

### Running the Web Application

1. Navigate to the project directory:
```bash
cd Car-Price-Prediction-Model-With-Frontend
```

2. Run the Streamlit app:
```bash
streamlit run frontend/stream.py
```

3. The application will open in your default browser at `http://localhost:8501`

### Using the Application

1. **Select Model**: Choose between Linear Regression or Random Forest
2. **Enter Car Details**:
   - Present Price (current showroom price)
   - Car Age (in years)
   - Kilometers Driven
   - Owner Type (First, Second, or Third+)
   - Fuel Type (Petrol, Diesel, CNG)
   - Seller Type (Dealer or Individual)
   - Transmission (Manual or Automatic)
3. **Click "Predict Price"**: Get instant price prediction
4. **View Results**: See estimated price, depreciation, and input summary

## 📁 Project Structure

```
Car-Price-Prediction-Model-With-Frontend/
│
├── code/
│   ├── clear_view.ipynb              # Data visualization
│   ├── data_understanding.ipynb       # Exploratory Data Analysis
│   ├── data_preprocessing.ipynb       # Data cleaning and encoding
│   ├── test_data.ipynb               # Test data generation
│   ├── testing_and_training_data+saving.ipynb  # Model training
│   └── using_saved_model.ipynb       # Model testing
│
├── files/
│   ├── car data.csv                  # Original dataset
│   ├── car_data_encoded.csv          # Encoded dataset
│   ├── car_data_new.csv              # Test data
│   ├── linear_model.pkl              # Saved Linear Regression model
│   └── rf_model.pkl                  # Saved Random Forest model
│
├── frontend/
│   └── stream.py                     # Streamlit web application
│
├── README.md                         # Project documentation
└── requirements.txt                  # Python dependencies
```

## 💻 Technologies Used

### Machine Learning
- **scikit-learn**: Model training and evaluation
- **pandas**: Data manipulation and analysis
- **pickle**: Model serialization

### Web Interface
- **Streamlit**: Interactive web application framework

### Data Processing
- **One-Hot Encoding**: Converting categorical variables to numerical
- **Train-Test Split**: 80-20 split for model validation

### Models
- **Linear Regression**: Baseline model for price prediction
- **Random Forest Regressor**: Advanced ensemble method with 200 trees

## 🔧 How It Works

### 1. Data Preprocessing
```python
# One-hot encoding for categorical variables
- Fuel_Type → Fuel_Type_Diesel, Fuel_Type_Petrol
- Seller_Type → Selling_type_Individual
- Transmission → Transmission_Manual

# Feature engineering
- Car_Age = Current_Year - Manufacturing_Year
```

### 2. Model Training
```python
# Linear Regression
- Simple linear relationship
- Fast training and prediction
- Good interpretability

# Random Forest
- 200 decision trees
- Ensemble averaging
- Captures non-linear patterns
```

### 3. Prediction Pipeline
```python
User Input → One-Hot Encoding → Model Prediction → Price Output
```

### 4. Web Interface
- Streamlit widgets for user input
- Real-time model selection
- Instant predictions with explanations

## 📸 Screenshots

### Main Interface
*Add screenshot of your Streamlit app main page*

### Prediction Results
*Add screenshot of prediction output with depreciation info*

### Input Details
*Add screenshot of the expandable input details section*

## 🚀 Future Improvements

- [ ] Add more car brands and models to the dataset
- [ ] Include additional features (engine size, horsepower, brand reputation)
- [ ] Implement advanced models (XGBoost, LightGBM)
- [ ] Add data visualization charts in the web interface
- [ ] Create API endpoint for mobile app integration
- [ ] Add model explainability features (SHAP values)
- [ ] Implement user authentication and history tracking
- [ ] Add comparison with market prices
- [ ] Include car condition assessment
- [ ] Multi-language support

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request


## 👨‍💻 Author

**Ibrahim**
- GitHub: [@Ibrahim-code21](https://github.com/Ibrahim-code21)

## 🙏 Acknowledgments

- Dataset source: Car price dataset from various Kaggle
- Inspiration: Real-world car valuation systems
- Libraries: scikit-learn, Streamlit, pandas communities

## 📞 Contact

For questions or feedback, please open an issue on GitHub or contact through the repository.

---

**⭐ If you find this project useful, please consider giving it a star!**

---

### Quick Start Commands

```bash
# Clone the repository
git clone https://github.com/Ibrahim-code21/Car-Price-Prediction-Model-With-Frontend.git

# Navigate to project
cd Car-Price-Prediction-Model-With-Frontend

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run frontend/stream.py
```

### Example Prediction

```
Input:
- Present Price: 10.0 Lakhs
- Car Age: 5 years
- Kilometers Driven: 50,000 km
- Owner: First Owner
- Fuel Type: Diesel
- Seller Type: Individual
- Transmission: Manual

Output (Random Forest):
- Estimated Selling Price: ₹7.48 Lakhs
- Depreciation: ₹2.52 Lakhs (25.2%)
```

---
