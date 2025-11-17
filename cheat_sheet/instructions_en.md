# Calculator CLI

A simple command-line calculator that performs basic mathematical operations.

## Quick Start

You'll find starter code templates in different folders based on the technology you want to use. Available templates include: `python/`, `flask/`, `django/`, `fastapi/`, `javascript/`, `typescript/`, `express/`, `react/`, `vue/`, `angular/`, and more. Pick the template folder you want to work with.

**Example using Python template:**

```bash
cd python

# Activate virtual environment (recommended)
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate     # On Windows

# Run the calculator
python main.py

# Deactivate virtual environment when done
deactivate
```

> **Note:** This project includes a `.venv` virtual environment for Python. Using a virtual environment is a best practice as it isolates project dependencies and prevents conflicts with other Python projects on your system.

## Templates

This project includes starter code templates for building the same calculator project using different technologies. Think of it as different doors to the same room - each language/framework has its own approach, but the end result is always a working calculator. Choose what interests you most!

### Available Templates

#### Python Ecosystem

- [x] **Python** - Pure Python implementation
- [ ] **Flask** - Web framework
- [ ] **Django** - Full-stack web framework
- [ ] **FastAPI** - Modern web framework
- [ ] **TensorFlow** - Machine learning framework
- [ ] **PyTorch** - Deep learning framework
- [ ] **Scikit-learn** - Machine learning library

#### JavaScript/Node.js Ecosystem

- [ ] **JavaScript** - Pure Node.js implementation
- [ ] **TypeScript** - Typed JavaScript superset
- [ ] **Express** - Web framework
- [ ] **React** - Frontend library
- [ ] **Vue** - Progressive framework
- [ ] **Angular** - Full-featured framework
- [ ] **TensorFlow.js** - ML in JavaScript

### Why Multiple Templates?

Each template shows different approaches to solving the same problem:

- **Learn variety**: See how different languages and frameworks handle the same task
- **Choose your stack**: Pick what you know or explore new tools
- **Compare**: Understand technology trade-offs
- **Practice**: Build skills with real industry tools

### How to Use Templates

1. Pick one template folder
2. Delete the others if you want
3. Explore the starter code in that folder
4. Complete the scaffolded starter code

All templates share the same requirements - only the implementation approach differs.

## Requirements

Build a CLI calculator that:

- Displays a menu with operations: Addition, Subtraction, Multiplication, Division, Exit
- Accepts two numbers from the user
- Validates input (re-prompt on errors)
- Handles division by zero
- Allows multiple calculations until user exits

## Implementation

**Tools:**

- `input()` / `float()` - get and convert user input
- `try-except` - handle errors gracefully
- `while` loop - repeat until user exits

**Steps:**

1. Create menu display function
2. Build operation functions: `add()`, `subtract()`, `multiply()`, `divide()`
3. Use try-except for input validation
4. Implement main loop with exit option

## Examples

### Addition

```
Enter your choice: 1
Enter first number: 15.5
Enter second number: 7.3
Result: 22.8
```

### Subtraction

```
Enter your choice: 2
Enter first number: 100
Enter second number: 45
Result: 55.0
```

### Multiplication

```
Enter your choice: 3
Enter first number: 6.5
Enter second number: 8
Result: 52.0
```

### Division

```
Enter your choice: 4
Enter first number: 100
Enter second number: 4
Result: 25.0
```

### Division by Zero

```
Enter your choice: 4
Enter first number: 50
Enter second number: 0
Error: Cannot divide by zero!
```

### Invalid Input

```
Enter first number: abc
Invalid input! Please enter a valid number.
Enter first number: 10
```

### Multiple Calculations

```
Enter your choice: 2
Enter first number: 100
Enter second number: 45
Result: 55.0

Do you want to perform another calculation? (yes/no): yes

Enter your choice: 3
Enter first number: 6.5
Enter second number: 8
Result: 52.0
```

### Exit

```
Enter your choice: 5
Thank you for using Calculator CLI!
```

---

## About

This project is part of the **BeCoder Community** - a learning platform dedicated to helping developers grow their skills through hands-on projects.

Visit us at: https://becoder.ro

## Rights

© 2025 BeCoder Community. All rights reserved.

This project and its contents are provided for educational purposes. You are free to use, modify, and distribute this project for learning and educational purposes. Please respect the BeCoder Community's contribution to the developer education community.
