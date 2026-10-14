# Lab 5: Static Code Analysis of a Restaurant Order System

## Project Overview
This project uses Python to implement a restaurant order management and billing system. Pylint, Bandit, and Flake8 are used to improve code quality, coding standards, and security.

## Objectives
- Identify code quality issues.
- Detect potential security vulnerabilities.
- Improve code readability and maintainability.
- Apply static code analysis tools.

## Technologies Used
- Python
- Pylint
- Bandit
- Flake8
- Git and GitHub

## Features
- Create and cancel restaurant orders.
- Check table order status.
- Calculate discounted bills.
- Generate SHA-256 ticket hashes.
- Generate secure POS PINs.
- Export kitchen orders.
- Count pending orders.

## Static Analysis Results
- Pylint: 10.00/10
- Bandit: No issues identified.
- Flake8: No style violations reported.

## How to Run
Install the tools:

```bash
python -m pip install pylint bandit flake8
```

Run the program:

```bash
python restaurant_order_system.py
```

Run the analysis tools:

```bash
python -m pylint restaurant_order_system.py
python -m bandit -r restaurant_order_system.py
python -m flake8 restaurant_order_system.py
```

## Conclusion
Static code analysis improved the security, readability, and maintainability of the restaurant order system.
