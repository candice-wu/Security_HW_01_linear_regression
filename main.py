import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.title('Interactive Linear Regression')

# Sidebar controls
st.sidebar.header('Parameters')
a = st.sidebar.slider('Slope (a)', 0.0, 10.0, 2.0)
noise = st.sidebar.slider('Noise', 0, 100, 25)
num_points = st.sidebar.slider('Number of points', 100, 1000, 500)

# Generate data
np.random.seed(0)
X = np.random.rand(num_points, 1) * 100
# The original equation was y = 2 * X + noise. We keep 'b' constant for simplicity.
y = a * X.squeeze() + np.random.randn(num_points) * noise

# Create and fit the model
model = LinearRegression()
model.fit(X, y)

# Predict
y_pred = model.predict(X)

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(X, y, color='blue', label='Data points')
ax.plot(X, y_pred, color='red', linewidth=2, label='Linear regression')
ax.set_title('Linear Regression')
ax.set_xlabel('X')
ax.set_ylabel('y')
ax.legend()
ax.grid(True)

# Display the plot in Streamlit
st.pyplot(fig)