import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Set random seed for reproducibility
np.random.seed(42)

# Define target fitting functions
def non_linear_func(x, a, b):
    """1 / (a + b*x)"""
    return 1 / (a + b * x)

def sinusoidal_func(x, A, omega, phi):
    """A * sin(omega * x + phi)"""
    return A * np.sin(omega * x + phi)

def power_law_func(x, a, b, c):
    """a * x^b + c"""
    return a * (x ** b) + c


def generate_data():
    """Generates synthetic noisy dataset for experiments."""
    x1 = np.linspace(1, 11, 50)
    y1 = non_linear_func(x1, a=2.0, b=0.5) + np.random.normal(0, 0.01, 50)

    x2 = np.linspace(0, 2 * np.pi, 50)
    y2 = sinusoidal_func(x2, A=2.0, omega=1.5, phi=0.5) + np.random.normal(0, 0.2, 50)

    x3 = np.linspace(1, 10, 50)
    y3 = power_law_func(x3, a=2.0, b=1.5, c=0.5) + np.random.normal(0, 1.0, 50)

    return (x1, y1), (x2, y2), (x3, y3)


def plot_fitting_results():
    (x1, y1), (x2, y2), (x3, y3) = generate_data()
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

    # 1. Non-linear Fitting
    popt1, _ = curve_fit(non_linear_func, x1, y1)
    axes[0].scatter(x1, y1, label="Noisy Data", color="green", alpha=0.7)
    axes[0].plot(x1, non_linear_func(x1, *popt1), label="Fitted Curve", color="red", linewidth=2)
    axes[0].set_title(r"$y = \frac{1}{a + bx}$")
    axes[0].legend()
    axes[0].grid(True, linestyle="--", alpha=0.6)

    # 2. Sinusoidal Fitting (with initial guess)
    popt2, _ = curve_fit(sinusoidal_func, x2, y2, p0=[2.0, 1.0, 0.0])
    axes[1].scatter(x2, y2, label="Noisy Data", color="green", alpha=0.7)
    axes[1].plot(x2, sinusoidal_func(x2, *popt2), label="Fitted Curve", color="red", linewidth=2)
    axes[1].set_title(r"$y = A \sin(\omega x + \phi)$")
    axes[1].legend()
    axes[1].grid(True, linestyle="--", alpha=0.6)

    # 3. Power Law Fitting
    popt3, _ = curve_fit(power_law_func, x3, y3)
    axes[2].scatter(x3, y3, label="Noisy Data", color="green", alpha=0.7)
    axes[2].plot(x3, power_law_func(x3, *popt3), label="Fitted Curve", color="red", linewidth=2)
    axes[2].set_title(r"$y = a x^b + c$")
    axes[2].legend()
    axes[2].grid(True, linestyle="--", alpha=0.6)

    plt.tight_layout()
    plt.savefig("result.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    plot_fitting_results()