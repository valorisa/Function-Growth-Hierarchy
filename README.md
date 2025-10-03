# Hiérarchie des Croissances des Fonctions

Ce document présente une **hiérarchie complète des fonctions par ordre de croissance**, depuis les fonctions constantes jusqu'aux fonctions au-delà de la tétration. Chaque fonction est expliquée avec des exemples concrets pour une compréhension claire.

---

## Hiérarchie Complète des Croissances (quand n → ∞)

### 1. Fonction Constante (croissance nulle)
- **Notation**: `c` (ex. : 1, 10, 100)
- **Exemple**: Complexité d’un accès à un tableau (O(1)).
- **Comportement**: Indépendante de `n`.

---

### 2. Fonctions Sous-linéaires (croissance très lente)
- **Logarithme**: `ln(n)` ou `log(n)`
  - **Exemple**: Complexité de la recherche dichotomique (O(log n)).
- **Racines**:
  - **Racine carrée**: `√n` ou `n^(1/2)`
    - **Exemple**: `√100 = 10`
  - **Racine cubique**: `∛n` ou `n^(1/3)`
    - **Exemple**: `∛27 = 3`
  - **Croissance**: Plus lente que linéaire, mais plus rapide que logarithmique.
- **Logarithme Itéré**: `log*(n)`
  - **Définition**: Nombre d’applications de `ln` pour obtenir un résultat ≤ 1.
  - **Exemple**: `log*(e^(e^(e^e))) = 4`
  - **Prononciation**: "log étoile de n".

---

### 3. Fonction Identité (croissance linéaire)
- **Notation**: `y = x` ou `f(n) = n`
- **Exemple**: Complexité d’une boucle sur `n` éléments (O(n)).

---

### 4. Fonctions Polynômiales (croissance modérée)
- **Notation**: `n^k` (ex. : `n^2`, `n^3`)
- **Exemple**: Complexité des algorithmes de tri naïfs (O(n^2)).

---

### 5. Fonctions Exponentielles (croissance rapide)
- **Exponentielle Simple**: `a^n` (ex. : `2^n`, `e^n`)
  - **Exemple**: Complexité du problème du voyageur de commerce par force brute.
- **Double Exponentielle**: `a^(a^n)` (ex. : `2^(2^n)`)

---

### 6. Fonctions Factorielles et Apparentées (croissance très rapide)
- **Primorielle**: `n#`
  - **Définition**: Produit des nombres premiers ≤ `n`.
  - **Exemple**: `10# = 2 × 3 × 5 × 7 = 210`
- **Factorielle**: `n!`
  - **Définition**: `n! = 1 × 2 × ... × n`
  - **Exemple**: `10! = 3,628,800`

---

### 7. Fonctions Super-Exponentielles (croissance explosive)
- **Super-Exponentielle**: `n^n`
  - **Exemple**: `10^10`
- **Tétration**: `n ↑↑ k`
  - **Définition**: Une "tour de puissances" de hauteur `k`.
  - **Exemple**: `3 ↑↑ 3 = 3^(3^3) = 7,625,597,484,987`

---

### 8. Fonctions au-delà de la Tétration (croissances "monstrueuses")
- **Flèches de Knuth**: `n ↑^k m`
  - **Exemple**: `3 ↑^3 2 = 3 ↑↑ (3 ↑↑ 3)`
- **Fonction d’Ackermann**: `A(n, n)`
  - **Exemple**: `A(4, 4)` est un nombre astronomique.
- **Flèches Chaînées de Conway**: `n → m → k`
  - **Exemple**: `3 → 3 → 3` dépasse toute imagination.
- **Fonction de Graham**: `G(n)`
  - **Exemple**: `G(1) = 3 ↑↑↑↑ 3`
- **Fonction TREE**: `TREE(n)`
  - **Exemple**: `TREE(3)` dépasse `G(64)`.
- **Fonction SCG**: `SCG(n)`
  - **Exemple**: Croissance encore plus rapide que `TREE(n)`.

---

## Résumé Visuel Complet (du plus lent au plus rapide)

```
c << ln(n) << n^(1/k) << log*(n) << n << n^k << a^n << n# << n! << n^n << n ↑↑ k << n ↑^k m << A(n, n) << n → m → k << G(n) << TREE(n) << SCG(n)
```

---

## Exemples Concrets pour n = 100

| Fonction               | Valeur pour n = 100                     | Croissance relative          |
|------------------------|------------------------------------------|-------------------------------|
| `c = 1`                | 1                                        | Constante                     |
| `ln(100)`              | ≈ 4.605                                  | Sous-linéaire                 |
| `√n`                   | 10                                       | Racine carrée                 |
| `∛n`                   | ≈ 4.64                                   | Racine cubique                |
| `log*(100)`            | 2                                        | Logarithme itéré              |
| `n = 100`              | 100                                      | Linéaire                      |
| `n^2 = 10000`          | 10000                                    | Polynomiale                   |
| `2^n`                  | ≈ 1.2677e+30                             | Exponentielle                 |
| `n#`                   | ≈ 2.3056e+153 (produit des 25 premiers nombres premiers ≤ 100) | Primorielle |
| `n!`                   | ≈ 9.3326e+157                             | Factorielle                   |
| `n^n`                  | 100^100                                  | Super-exponentielle           |

---

## Pourquoi cette Hiérarchie est Importante ?

1. **En algorithmique**: Elle permet de classer les algorithmes par efficacité.
2. **En analyse asymptotique**: Elle aide à déterminer la convergence des séries ou des suites.
3. **En théorie des nombres et combinatoire**: Elle permet de comprendre la taille des objets (ex. : nombres premiers, graphes).
4. **En logique et informatique théorique**: Les fonctions au-delà de la tétration illustrent les limites des systèmes formels et des hiérarchies de complexité.



## Licence

Ce projet est sous licence [MIT](LICENSE).
