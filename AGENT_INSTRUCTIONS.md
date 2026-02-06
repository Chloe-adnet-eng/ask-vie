# Instructions pour les Agents - ask-vie Project

## 1. Contexte du Projet

**Objectif**: Construire un RAG (Retrieval-Augmented Generation) qui permet de poser des questions sur des documents de contrat VIE (Volontariat International en Entreprise).

**Stack Technique**:
Toujours lire les fichiers pour connaitre la stack technique du projet la plus à jour.

**Localisation**: `/Users/chloeadnet/Desktop/PERSO/DEV/ask-vie`

---

## 2. Processus Obligatoire Avant Toute Action

### 2.1 Phase de Recherche et Compréhension
1. **Lire l'ensemble des fichiers du projet** : parcourir tous les fichiers de ask-vie
2. **Consulter la documentation officielle** pour chaque technologie concernée
3. **Analyser la structure existante** et les patterns en place
4. **Identifier les dépendances** et contraintes avant toute décision
5. **Vérifier la compatibilité** avec les versions Python et les dépendances

### 2.2 Décision et Conception
- Si plusieurs approches sont possibles, analyser les **avantages et inconvénients**
- Consulter les ressources **software craftsmanship** pour les refactorings
- Justifier les choix technologiques

---

## 3. Gestion des Tests (Obligatoire)

### 3.1 Structure des Tests
- **Localisation**: `tests/` à la racine du projet
- **Organisation**: Miroir la structure de `src/`
- **Framework**: pytest
- **Nommage**: `test_<module_name>.py
utiliser les ressources officielles de pytest tout le temps

### 3.2 Méthodologie Given-When-Then
```python
# Template obligatoire pour chaque test
def test_feature_description():
    """
    Given: Description de l'état initial/contexte
    When: Action/événement
    Then: Résultat attendu
    """
    # GIVEN - Arrange
    initial_state = ...

    # WHEN - Act
    result = function_under_test(initial_state)

    # THEN - Assert
    assert result == expected_value
```

### 3.3 Exigences de Test
- **100% de couverture** pour les nouvelles fonctionnalités
- **Tests unitaires** pour chaque fonction
- **Pas de commit sans tests passants**

### 3.4 Lancer les Tests
```bash
# Avant chaque proposition de modification
pytest
pytest --cov=src  # Avec couverture
```

---

## 4. Pre-commit Obligatoire

### 4.1 Configuration
- Un fichier `.pre-commit-config.yaml` doit exister et être maintenu
- Hooks obligatoires : linting, formatting, security checks

### 4.2 Avant Chaque Proposition
```bash
# Vérifier que les pre-commit passent
pre-commit run --all-files
```

- **Aucune proposition ne peut être faite si pre-commit échoue**
- Corriger les problèmes automatiquement si possible

---

## 5. Refactoring et Software Craftsmanship

### 5.1 Avant Tout Refactoring
Consulter :
- **Clean Code** (Robert C. Martin)
- **Patterns et bonnes pratiques Python** (PEP 8, PEP 20)
- **SOLID Principles**
- **DRY, KISS, YAGNI**

### 5.2 Processus Obligatoire
1. Analyser la **documentation de software craftsmanship** applicable
2. Identifier la **méthode la plus adaptée** au contexte
3. Proposer une solution avec **justification**
4. Implémenter **progressivement** avec tests
5. Valider que **tous les tests restent verts**

### 5.3 Critères de Qualité
- Code lisible et maintenable
- Fonctions avec une **responsabilité unique**
- Documentation des décisions complexes
- Pas de code mort ou dupliqué
- Types documentés (type hints)

---

## 6. Workflow de Développement

### 6.1 Pour Chaque Tâche
```
1. Lire les fichiers pertinents
2. Consulter la documentation officielle
3. Proposer l'approche
4. Implémenter avec tests
5. Vérifier: pytest ✓
6. Vérifier: pre-commit ✓
7. Proposer la solution
```

### 6.2 Implémentation
- Créer les tests **en premier** (TDD recommandé)
- Implémenter la fonctionnalité
- S'assurer que tous les tests passent
- Refactoriser si nécessaire
- Vérifier la couverture

### 6.3 Validation Final
```bash
# Avant toute proposition
pytest                          # Tests passants ✓
pytest --cov=src               # Couverture acceptable ✓
pre-commit run --all-files     # Tous les checks passent ✓
```

---

## 7. Contraintes Spécifiques du Projet

### 7.1 Gestion des Clés API
- **Pas de clé API actuellement disponible**
- Utiliser des **modèles locaux** si nécessaire (llama, gpt4all, etc.)
- Implémenter l'abstraction pour **ajouter les clés API ultérieurement**
- Utiliser des variables d'environnement pour les secrets

### 7.2 RAG (Retrieval-Augmented Generation)
- Architecture générique pour supporter différentes sources
- Séparation claire entre **retrieval** et **generation**
- Tests pour chaque composant du RAG
- Documentations des workflows

---
## 10. Ressources de Référence
toujours consulter les ressources web officielles et leur derniere version, ne jamais se reposer sur de la connaissance aquise.
