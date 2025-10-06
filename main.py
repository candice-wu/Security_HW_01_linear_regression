import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd

st.title('Interactive Linear Regression')

# Sidebar controls
st.sidebar.header('Parameters')
a = st.sidebar.slider('Coefficient \'a\' (y = ax + b + noise)', 0.0, 10.0, 2.0)
noise = st.sidebar.slider('Noise Variance (var)', 0, 100, 25)
num_points = st.sidebar.slider('Number of points', 100, 1000, 500)

# Generate data
np.random.seed(0)
X = np.random.rand(num_points, 1) * 100
y = a * X.squeeze() + np.random.randn(num_points) * noise

# Create and fit the model
model = LinearRegression()
model.fit(X, y)

# Predict
y_pred = model.predict(X)

# --- Plot ---

# Calculate residuals and find outliers
residuals = y - y_pred
outlier_indices = np.argsort(np.abs(residuals))[-5:]

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot all data points
ax.scatter(X, y, color='pink', label='Data points')

# Highlight outliers
ax.scatter(X[outlier_indices], y[outlier_indices], color='lightsteelblue', s=100, label='Top 5 Outliers', edgecolors='red')

# Plot the regression line
ax.plot(X, y_pred, color='darkviolet', linewidth=2, label='Linear regression')

ax.set_title('Interactive Linear Regression with Top 5 Outliers')
ax.set_xlabel('X')
ax.set_ylabel('y')
ax.legend()
ax.grid(True)

# Display the plot in Streamlit
st.pyplot(fig)

# --- Information Below Plot ---

col1, col2 = st.columns(2)

with col1:
    # 1. Display Model Coefficients
    st.subheader('Model Coefficients')
    st.write(f'**Slope (Coefficient):** {model.coef_[0]:.4f}')
    st.write(f'**Intercept:** {model.intercept_:.4f}')

with col2:
    # 2. Identify and Display Top 5 Outliers
    st.subheader('Top 5 Outliers')
    outliers = pd.DataFrame({
        'X': X.squeeze()[outlier_indices],
        'y': y[outlier_indices],
        'Predicted y': y_pred[outlier_indices],
        'Residual': residuals[outlier_indices]
    })
    st.write(outliers)