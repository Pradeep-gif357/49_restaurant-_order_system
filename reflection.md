# Reflection — Lab 5: Static Code Analysis

The uploaded lab handout refers to four reflection questions, but their exact wording is not visible in the provided handout. The following are suggested answers to common reflection prompts; adjust them to match the exact questions your instructor gives you.

## 1. What is static code analysis?

Static code analysis examines source code without executing the program. It can detect possible bugs, insecure coding patterns, maintainability problems, and style violations early in development.

## 2. What is the difference between Pylint, Bandit, and Flake8?

Pylint checks code quality and programming practices, including naming, unused variables, and possible logic problems. Bandit searches Python code for common security risks. Flake8 checks style and related issues such as whitespace, line length, and unused imports.

## 3. What issues did you find and fix?

The original restaurant order program contained a dangerous use of `eval()` for discount calculation, a shell command built using a filename, a hard-coded secret printed to output, predictable PIN generation, a mutable default list, and a broad exception handler that silently ignored errors. The revised version removes dynamic evaluation and shell execution, removes the embedded secret, uses `secrets` for PIN generation, avoids a mutable default, and handles missing orders without suppressing arbitrary exceptions. It also replaces MD5 with SHA-256, removes unused code, and uses a context-safe file-writing method.

## 4. How did static analysis improve the program?

Static analysis helped identify security, reliability, and maintainability problems that might not be obvious when the program appears to run successfully. Fixing these issues makes the code easier to read and maintain and reduces avoidable security risks. The program must still be run and tested because static analysis cannot prove that all logic is correct.
