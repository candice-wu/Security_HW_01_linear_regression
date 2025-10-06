Demosite：https://securityhw01linearregression-o9pd5qxrsr7c5y6qpjfhrv.streamlit.app

# Interactive Linear Regression Application

This project is a simple web application that demonstrates linear regression. It's built using Python, Streamlit, scikit-learn, and Matplotlib. The application allows users to interactively adjust parameters and see how they affect the regression model in real-time.

## CRISP-DM Framework

We'll use the Cross-Industry Standard Process for Data Mining (CRISP-DM) framework to describe the project.

### 1. Business Understanding

The primary goal of this project is to provide an educational tool for understanding the fundamentals of linear regression. Users can visually comprehend the impact of the slope of the regression line, the amount of noise in the data, and the number of data points on the model's fit.

### 2. Data Understanding

The data for this project is synthetically generated. We create a set of data points (X, y) where:

- **X:** A series of random numbers representing the independent variable.
- **y:** The dependent variable, calculated as `y = a * X + noise`, where `a` is the slope.

The user can control the values of `a`, the amount of `noise`, and the `number of points` through the application's interface.

### 3. Data Preparation

The data is generated and prepared on-the-fly within the application. Based on the user's input from the Streamlit sidebar controls, a new dataset is created for each change. This immediate feedback loop means there is no need for a separate, offline data preparation step.

### 4. Modeling

We use a simple linear regression model from the `scikit-learn` library. The model learns the relationship between `X` and `y` and calculates the best-fit line that minimizes the sum of the squared differences between the actual and predicted `y` values.

### 5. Evaluation

Evaluation in this application is primarily visual. The application plots:

- The raw data points (a scatter plot).
- The linear regression line (a line plot).

By observing how the line fits the data as they adjust the parameters, users can intuitively evaluate the model's performance under different conditions.

### 6. Deployment

The application is deployed locally using Streamlit. To run the application, you need to have Python and the required libraries installed.

**To run the app:**

1.  **Install the dependencies:**

    ```bash
    pip install streamlit scikit-learn matplotlib
    ```

2.  **Run the application:**

    ```bash
    streamlit run main.py
    ```

This will start a local web server and open the application in your browser.