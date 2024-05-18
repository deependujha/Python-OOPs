# Class methods & static methods

A class can contains 3 types of methods:
    - instance method (automatically passes instance as first argument)
    - class method (automatically passes class itself as first argument)
    - static method (similar to a normal method, only grouped together with a class because of semantic meaning)

---

## Decorators

- **Instance methods**: no decorators required (**`default`**)
- **Class methods**: **`@classmethod`**
- **Staic methods**: **`@staticmethod`**

---

## First argument

- **Instance methods**: **`self`**
- **Class methods**: **`cls`**
- **Static methods**: none, depends on you.
