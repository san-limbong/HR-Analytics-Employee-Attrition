import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder

# Function to label encode specified columns
def label_encode_columns(dataframe, columns):
    le = LabelEncoder()
    for column in columns:
        # Check if the column contains any non-numeric values
        if not pd.api.types.is_numeric_dtype(dataframe[column]):
            # If not numeric, convert the column to string before applying LabelEncoder
            dataframe[column] = dataframe[column].astype(str)

        dataframe[column] = le.fit_transform(dataframe[column])
    return dataframe

# Load the trained model from file
filename = 'model.joblib'
loaded_model = joblib.load(filename)

# Define columns to encode
columns_to_encode = ['BusinessTravel', 'Department', 'Gender']

# Generate new data for prediction randomize
# Age = np.random.randint(18, 95)
# BusinessTravel = np.random.choice(['Non-Travel', 'Travel_Frequently', 'Travel_Rarely'])
# Department = np.random.choice(['Research & Development', 'Human Resources', 'Sales'])
# DistanceFromHome = np.random.randint(1, 30)
# Education = np.random.randint(1, 5)
# EnvironmentSatisfaction = np.random.randint(1, 4)
# Gender = np.random.choice(['Male', 'Female'])
# PerformanceRating = np.random.randint(3, 4)
# WorkLifeBalance = np.random.randint(1, 4)

# Input
Age = int(input("Age[18-65]: "))
BusinessTravel = input("BusinessTravel['Non-Travel', 'Travel_Frequently', 'Travel_Rarely']: ")
Department = input("Department['Research & Development', 'Human Resources', 'Sales']: ")
DistanceFromHome = int(input("DistanceFromHome[1-30]: "))
Education = int(input("Education[1-5]: "))
EnvironmentSatisfaction = int(input("EnvironmentSatisfaction[1-4]: "))
Gender = input("Gender['Male', 'Female']: ")
PerformanceRating = int(input("PerformanceRating[3,4]: "))
WorkLifeBalance = int(input("WorkLifeBalance[1-4]: "))

# yes example
# Age = 18
# BusinessTravel = 'Travel_Rarely'
# Department = 'Research & Development'
# DistanceFromHome = 2
# Education = 2
# EnvironmentSatisfaction = 2
# Gender = 'Male'
# PerformanceRating = 2
# WorkLifeBalance = 2

# Create a new dataframe with the input data
new_data = pd.DataFrame([[Age, BusinessTravel, Department, DistanceFromHome,
                          Education, EnvironmentSatisfaction, Gender, PerformanceRating, WorkLifeBalance]],
                        columns=['Age', 'BusinessTravel', 'Department', 'DistanceFromHome', 
                                 'Education', 'EnvironmentSatisfaction', 'Gender', 'PerformanceRating', 'WorkLifeBalance'])

# Apply label encoding to the new data
new_data_encoded = label_encode_columns(new_data, columns_to_encode)

# Predict using the loaded model
prediction = loaded_model.predict(new_data_encoded)

# Output prediction result
if prediction == 1:
    print('Yes') # or 1
else:
    print('No') # or 0
