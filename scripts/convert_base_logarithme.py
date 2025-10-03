import math

# Codes de couleur ANSI
RED = '\033[91m'
RESET = '\033[0m'

def log_base_n(x, base):
    """Calcule le logarithme de x en base 'base'."""
    return math.log(x) / math.log(base)

def log_star(n):
    """Calcule le logarithme itéré de n en base 2."""
    if n <= 1:
        return 0
    else:
        return 1 + log_star(math.log2(n))

def afficher_menu():
    """Affiche le menu principal avec le titre en rouge."""
    print(f"\n" + "="*40)
    print(f"{RED} MENU DES FONCTIONS LOGARITHMIQUES {RESET}")
    print("="*40)
    print("1. Calculer un logarithme dans une base donnée")
    print("2. Convertir un logarithme d'une base à une autre")
    print("3. Calculer le logarithme itéré (log*)")
    print("4. Afficher l'historique des calculs")
    print("5. Afficher les propriétés des logarithmes")
    print("6. Quitter")
    print("="*40)

def get_float_input(prompt):
    """Demande une entrée numérique à l'utilisateur, accepte les virgules."""
    while True:
        try:
            value = input(prompt).replace(',', '.')
            return float(value)
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")

def get_base_input(prompt):
    """Demande une base à l'utilisateur, accepte 'e' pour la base e."""
    while True:
        base_input = input(prompt).strip().lower()
        if base_input == 'e':
            return math.e
        try:
            base_input = base_input.replace(',', '.')
            base = float(base_input)
            if base <= 0 or base == 1:
                print("Erreur : La base doit être un nombre positif différent de 1.")
            else:
                return base
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide ou 'e' pour la base e.")

historique = []

def ajouter_historique(operation, resultat):
    historique.append((operation, resultat))

def afficher_historique():
    print("\n--- Historique des Calculs ---")
    if not historique:
        print("Aucun calcul enregistré.")
    else:
        for i, (operation, resultat) in enumerate(historique, 1):
            print(f"{i}. {operation} = {resultat:.6f}")

def afficher_proprietes():
    print("\n--- Propriétés des Logarithmes ---")
    print("1. log_b(b) = 1")
    print("2. log_b(1) = 0")
    print("3. log_b(x * y) = log_b(x) + log_b(y)")
    print("4. log_b(x / y) = log_b(x) - log_b(y)")
    print("5. log_b(x^y) = y * log_b(x)")
    print("6. Changement de base : log_b(x) = log_k(x) / log_k(b)")

def calculer_logarithme():
    """Calcule un logarithme dans une base donnée."""
    print("\n--- Calcul d'un logarithme ---")
    x = get_float_input("Entrez la valeur de x : ")
    base = get_base_input("Entrez la base du logarithme (ou 'e' pour la base e) : ")
    resultat = log_base_n(x, base)
    operation = f"log_{base}({x})"
    ajouter_historique(operation, resultat)
    print(f"\nRésultat : {operation} = {resultat:.6f}")

def convertir_logarithme():
    """Convertit un logarithme d'une base à une autre."""
    print("\n--- Conversion de logarithme ---")
    x = get_float_input("Entrez la valeur de x : ")
    from_base = get_base_input("Entrez la base actuelle du logarithme (ou 'e' pour la base e) : ")
    to_base = get_base_input("Entrez la nouvelle base du logarithme (ou 'e' pour la base e) : ")
    resultat = log_base_n(x, from_base)
    resultat_converti = log_base_n(x, to_base)
    operation1 = f"log_{from_base}({x})"
    operation2 = f"log_{to_base}({x})"
    ajouter_historique(operation1, resultat)
    ajouter_historique(operation2, resultat_converti)
    print(f"\nRésultats :")
    print(f"{operation1} = {resultat:.6f}")
    print(f"{operation2} = {resultat_converti:.6f}")

def calculer_log_star():
    """Calcule le logarithme itéré de n."""
    print("\n--- Calcul du logarithme itéré ---")
    n = get_float_input("Entrez la valeur de n : ")
    resultat = log_star(n)
    operation = f"log*({n})"
    ajouter_historique(operation, resultat)
    print(f"\nRésultat : {operation} = {resultat}")

def main():
    """Fonction principale pour gérer le menu."""
    while True:
        afficher_menu()
        choix = input("\nChoisissez une option (1-6) : ").strip()
        if choix == "1":
            calculer_logarithme()
        elif choix == "2":
            convertir_logarithme()
        elif choix == "3":
            calculer_log_star()
        elif choix == "4":
            afficher_historique()
        elif choix == "5":
            afficher_proprietes()
        elif choix == "6":
            print("\nAu revoir !")
            break
        else:
            print("Option invalide. Veuillez choisir une option entre 1 et 6.")

if __name__ == "__main__":
    main()
