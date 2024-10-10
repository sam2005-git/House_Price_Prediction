import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# Load the dataset (ensure 'house_data.csv' is in the same directory or provide the correct path)
data = pd.read_csv('house_data.csv')

# Select features and target (modify columns based on your CSV file)
X = data[['Area', 'Bedrooms', 'Bathrooms']]  # Example features
y = data['Price']  # Target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Save the trained model
joblib.dump(model, 'house_price_model.pkl')
