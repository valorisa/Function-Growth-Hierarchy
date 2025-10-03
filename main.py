from scripts.compare_growth import print_function_values
from scripts.plot_growth import plot_function_growth

def main():
    """Fonction principale pour exécuter les scripts du projet."""
    print_function_values(100)
    print_function_values(10000)
    plot_function_growth()

if __name__ == "__main__":
    main()
