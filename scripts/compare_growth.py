import math

def calculate_functions(n):
    """Calcule les valeurs des fonctions pour une valeur donnée de n."""
    functions = {
        "ln(n)": math.log(n),
        "√n": math.sqrt(n),
        "∛n": n ** (1/3),
        "n": n,
        "n^2": n ** 2,
        "2^n": 2 ** n,
    }
    return functions

def print_function_values(n):
    """Affiche les valeurs des fonctions pour une valeur donnée de n."""
    values = calculate_functions(n)
    print(f"\nValeurs des fonctions pour n = {n}:")
    for func, value in values.items():
        print(f"{func}: {value}")

if __name__ == "__main__":
    # Exemples d'utilisation
    print_function_values(100)
    print_function_values(10000)
