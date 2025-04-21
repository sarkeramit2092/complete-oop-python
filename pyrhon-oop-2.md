# Class Diagram

## Class: Car

### Private Attributes:
- `color`
- `mileage`
- `engine`

### Public Methods:
- `cal_avg_speed()`
- `open_airbag()`
- `show_gps()`

---

# Object Examples

> Object is an instance of the class.  
> Class names should be in **PascalCase** (e.g., `ThisIsPascalCase`).

1. **Class**: `Car` → **Object**: `WagonR`  
   **Code**: `wagonr = Car()`

2. **Class**: `Sports` → **Object**: `Gilli Danda`  
   **Code**: `gillidanda = Sports()`

3. **Class**: `Animals` → **Object**: `Langoor`  
   **Code**: `langoor = Animals()`

---

# Function vs Methods

- **Methods** are basically functions written **inside** a class.
- **Functions** are standalone and **not** part of a class.

Examples:
```python
len(L)        # function
L.append(1)   # method, L is a list here
```

---

# Object Literal

Object literals are an easy way to make objects from a class.

Example:
```python
l = list(1, 3, 4, 6, 7)
# Same as:
l = [1, 3, 4, 6, 7]
```

- `list()`, `str()` etc. are **built-in classes** in Python.
- Python provides a simpler syntax (object literals) for these built-in classes.

---

# Let's Make a Class

## Class: ATM

### Attributes:
- `PIN`
- `Balance`

### Methods:
- `create_pin()`
- `withdraw()`
- `check_balance()`
- `deposit()`
