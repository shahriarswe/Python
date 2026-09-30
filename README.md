# Python OOP – 50 Solved Problems

A single, well-organized Python script covering **50 solved Object-Oriented
Programming problems**, from basics to design patterns. Great for practice,
interview prep, or as a personal reference — and it's a free, public repo,
so there's no cost or limit to using or sharing it on GitHub.

## 📂 Contents

Split into 5 files, 10 problems each, so each part can be run independently:

- `part1_problems_01_10.py` – Section 1: OOP Basics
- `part2_problems_11_20.py` – Section 2: Encapsulation
- `part3_problems_21_30.py` – Section 3: Inheritance
- `part4_problems_31_40.py` – Section 4: Polymorphism & Abstraction
- `part5_problems_41_50.py` – Section 5: Advanced OOP
- `python_oop_50_solved.py` – all 50 problems combined in a single file, if
  you prefer one file over five
- `README.md` – this file

## ▶️ How to run

Requires only Python 3 (no external packages). Each part is self-contained:

```bash
python3 part1_problems_01_10.py
python3 part2_problems_11_20.py
python3 part3_problems_21_30.py
python3 part4_problems_31_40.py
python3 part5_problems_41_50.py
```

Or run the combined file instead:

```bash
python3 python_oop_50_solved.py
```

Each prints the output of its demos in order, prefixed with the problem
number (e.g. `01:`, `02:`, ...).

## 📋 Problem list

### Section 1 — OOP Basics (01–10)
1. Simple class with attributes and a method
2. Class variables vs. instance variables
3. Constructor with default arguments
4. `__str__` and `__repr__`
5. A method that mutates instance state (bank account deposit/withdraw)
6. Multiple objects tracked in a list
7. Destructor (`__del__`)
8. Method chaining using `self`
9. Class method as an alternate constructor
10. Type and identity checks (`type()`, `is`)

### Section 2 — Encapsulation (11–20)
11. Private attribute with name mangling
12. Protected attribute convention (`_single_underscore`)
13. `@property` for a computed read-only attribute
14. Getter/setter with validation via `@property.setter`
15. Read-only property with no setter
16. Encapsulating a list to prevent direct external modification
17. Hiding internal state behind a public API (stack push/pop)
18. Encapsulation combined with constructor validation
19. Accessing a name-mangled attribute (education only)
20. Property derived from two private parts (full name)

### Section 3 — Inheritance (21–30)
21. Basic single inheritance
22. `super()` to extend a parent constructor
23. Multilevel inheritance
24. Multiple inheritance
25. Method overriding with a call back to the parent
26. MRO (Method Resolution Order) with diamond inheritance
27. Abstract-ish base using `NotImplementedError`
28. Overriding `__init__` across three generations
29. `isinstance()` and `issubclass()`
30. Extending a built-in type (`list`)

### Section 4 — Polymorphism & Abstraction (31–40)
31. Simple polymorphism (same method name, different behavior)
32. Duck typing (no shared base class)
33. Abstract Base Class (`ABC`) forcing implementation
34. Operator overloading with `__add__`
35. Operator overloading with `__eq__` and `__lt__`
36. Polymorphism through a common interface in a loop
37. Abstract class with both abstract and concrete methods
38. `__len__` and `__getitem__` (sequence-like behavior)
39. `__call__` to make instances callable
40. Instantiating an ABC directly raises `TypeError`

### Section 5 — Advanced OOP (41–50)
41. Static method
42. Class method using class-level state
43. Composition (has-a relationship)
44. Custom exception classes
45. Singleton design pattern
46. Custom iterator (`__iter__` / `__next__`)
47. Custom context manager (`__enter__` / `__exit__`)
48. Mixin classes for reusable behavior
49. Factory design pattern
50. Combined example: inheritance + encapsulation + abstraction + polymorphism

## 🚀 Push this to GitHub

If you'd like to publish this as your own repo:

```bash
git init
git add .
git commit -m "Add 50 solved Python OOP problems"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git push -u origin main
```

Creating a public repository like this is completely free on GitHub — no
storage or usage limits apply for a small text-based project like this one.

