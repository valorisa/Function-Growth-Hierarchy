# Function-Growth-Hierarchy

**Une hiérarchie complète des fonctions par ordre de croissance, des constantes aux fonctions au-delà de la tétration.**

---

## Description

Ce projet présente une hiérarchie complète des fonctions mathématiques par ordre de croissance. Il inclut des scripts pour comparer et visualiser les croissances des fonctions, ainsi que des tests pour valider les calculs.

---

## Fonctions Incluses

- **Fonctions constantes** : \( c \)
- **Fonctions sous-linéaires** : \( \ln(n) \), \( \log_{10}(n) \), \( \sqrt{n} \), \( \sqrt[3]{n} \)
- **Fonctions linéaires** : \( n \)
- **Fonctions polynômiales** : \( n^k \)
- **Fonctions exponentielles** : \( a^n \)
- **Fonctions factorielles et apparentées** : \( n! \), \( n\# \)
- **Fonctions super-exponentielles** : \( n^n \), tétration
- **Fonctions au-delà de la tétration** : flèches de Knuth, fonction d'Ackermann, flèches chaînées de Conway, fonction de Graham, fonction TREE, fonction SCG

---

## Structure du Projet

```
.
├── LICENSE
├── alt_Readme.md
├── README.md
├── requirements.txt
├── setup.py
├── main.py
├── scripts
│   ├── __init__.py
│   ├── compare_growth.py
│   └── plot_growth.py
└── tests
    └── test_functions.py
```

---

## Installation

### Prérequis

- Python 3.6 ou supérieur
- Pip (pour installer les dépendances)

### Étapes d'installation

1. Clone le dépôt :

```bash
git clone https://github.com/valorisa/Function-Growth-Hierarchy.git
cd Function-Growth-Hierarchy
```

2. Installe les dépendances :

```bash
pip install -r requirements.txt
```

3. (Optionnel) Installe le projet en tant que package Python :

```bash
pip install .
```

---

## Utilisation

### Comparer les valeurs des fonctions

Pour comparer les valeurs des fonctions pour différentes valeurs de `n`, exécute :

```bash
python scripts/compare_growth.py
```

#### Exemple de sortie :

```
Valeurs des fonctions pour n = 100:
    ln(n): 4.605170185988092
   √2n: 10.0
    ∛n: 4.641588833612778
       n: 100
    n^2: 10000
    2^n: 1267650600228229401496703205376

Valeurs des fonctions pour n = 10000:
    ln(n): 9.210340371976184
   √2n: 100.0
    ∛n: 21.544346900318832
       n: 10000
    n^2: 100000000
    2^n: Trop grand (≈ 3011 chiffres)
```

---

### Visualiser les croissances des fonctions

Pour visualiser les croissances des fonctions, exécute :

```bash
python scripts/plot_growth.py
```

Cela ouvrira une fenêtre avec un graphique montrant les croissances des fonctions \( \ln(n) \), \( \sqrt{n} \), \( \sqrt[3]{n} \), \( n \), et \( n^2 \).

---

### Exécuter le projet via main.py

Pour exécuter le projet avec les paramètres par défaut, utilise :

```bash
python main.py
```

Cela affichera les valeurs des fonctions pour `n = 100` et `n = 10000`, et ouvrira un graphique montrant les croissances des fonctions.

---

### Exécuter les tests

Pour exécuter les tests et vérifier que tout fonctionne correctement, exécute :

```bash
python -m unittest discover tests
```

#### Exemple de sortie :

```
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

---

## Exemples Avancés

### Utiliser des paramètres personnalisés

Tu peux personnaliser les paramètres `a` et `k` pour les fonctions exponentielles et les racines :

```python
from scripts.compare_growth import print_function_values

# Exemple avec a=3 et k=4
print_function_values(100, a=3, k=4)
```

---

## Installation via pip

Tu peux installer ce projet en tant que package Python avec pip :

```bash
pip install .
```

---

## Contribuer

Les contributions sont les bienvenues ! Voici comment contribuer :

1. Fork le projet.
2. Crée une branche pour ta fonctionnalité (`git checkout -b feature/ma-nouvelle-fonctionnalité`).
3. Commit tes modifications (`git commit -am 'Ajout d'une nouvelle fonctionnalité'`).
4. Push vers la branche (`git push origin feature/ma-nouvelle-fonctionnalité`).
5. Ouvre une Pull Request.

---

## Licence

Ce projet est sous licence [MIT](LICENSE).
```
