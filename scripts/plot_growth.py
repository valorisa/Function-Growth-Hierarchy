import matplotlib.pyplot as plt
import numpy as np
import math

def plot_function_growth():
    n_values = np.linspace(1, 100, 1000)

    plt.figure(figsize=(12, 8))

    plt.plot(n_values, np.log(n_values), label='ln(n)')
    plt.plot(n_values, np.sqrt(n_values), label='√n')
    plt.plot(n_values, n_values ** (1/3), label='∛n')
    plt.plot(n_values, n_values, label='n')
    plt.plot(n_values, n_values ** 2, label='n^2')

    plt.yscale('log')
    plt.xscale('log')
    plt.xlabel('n')
    plt.ylabel('Valeur')
    plt.title('Croissance des fonctions')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_function_growth()
