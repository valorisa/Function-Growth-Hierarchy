import math

def calculate_functions(n, a=2, k=2):
    """
    Calcule les valeurs des fonctions pour une valeur donnée de n.

    Args:
        n (int): La valeur pour laquelle calculer les fonctions.
        a (int, optional): La base pour la fonction exponentielle. Par défaut, 2.
        k (int, optional): Le degré de la racine. Par défaut, 2.

    Returns:
        dict: Un dictionnaire contenant les valeurs des fonctions.
    """
    functions = {
        "ln(n)": math.log(n),
        f"√{k}n": n ** (1/k),
        "∛n": n ** (1/3),
        "n": n,
        "n^2": n ** 2,
        "log10(n)": math.log10(n),
    }

    # Gestion spéciale pour a^n
    power = a ** n
    if len(str(power)) > 50:
        num_digits = len(str(power))
        functions[f"{a}^n"] = f"Trop grand (≈ {num_digits} chiffres)"
    else:
        functions[f"{a}^n"] = power

    return functions

def print_function_values(n, a=2, k=2):
    """
    Affiche les valeurs des fonctions pour une valeur donnée de n.

    Args:
        n (int): La valeur pour laquelle afficher les fonctions.
        a (int, optional): La base pour la fonction exponentielle. Par défaut, 2.
        k (int, optional): Le degré de la racine. Par défaut, 2.
    """
    values = calculate_functions(n, a, k)
    print(f"\nValeurs des fonctions pour n = {n}:")
    for func, value in values.items():
        print(f"{func:>10}: {value}")

if __name__ == "__main__":
    # Exemples d'utilisation
    print_function_values(100)
    print_function_values(10000)
