# Non-Linear Curve Fitting with SciPy and NumPy

This project demonstrates non-linear optimization and mathematical curve fitting techniques using Python's `scipy.optimize.curve_fit`, `numpy`, and `matplotlib`.

## 📌 Features
- Generates synthetic noisy datasets for mathematical experimentation.
- Fits mathematical models to synthetic data using non-linear least squares optimization:
  1. Rational / Inverse Function: y = 1 / (a + b*x)
  2. Sinusoidal Wave Function: y = A * sin(omega * x + phi)
  3. Power Law Function with Offset: y = a * x^b + c
- Visualizes fitting curves against original noisy data points.

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/diako-t/non-linear-curve-fitting.git]
   cd non-linear-curve-fitting
2. Install dependencies:
   pip install -r requirements.txt
3. Run the script:
   python main.py