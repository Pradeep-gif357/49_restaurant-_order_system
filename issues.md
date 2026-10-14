# Static Code Analysis Issues — Restaurant Order System

> Line numbers below refer to the original `restaurant_order_system.py` uploaded for this lab. Recheck line numbers if the original file has changed. Severity labels are practical prioritization for this lab; Bandit may assign its own severity/confidence ratings.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Dynamic `eval()` in discount calculation | Security / High | 40–43 | Evaluating a supplied expression can execute arbitrary Python code if the expression is untrusted. | Removed expression evaluation. The function accepts a numeric discount rate and validates that it is between 0 and 1. |
| Shell command built from filename | Security / High | 54–58 | Passing a filename into `os.system()` can create command-injection risk and is unnecessary for this program. | Removed the shell command and log a message using Python's logging module. |
| Hard-coded POS secret | Security / High | 69–80 | A secret is embedded in source code and printed, exposing it to anyone who can read program output or source. | Removed the hard-coded secret and stopped printing it. A real deployment should load secrets from a protected environment/configuration source. |
| Predictable PIN generation | Security / Medium | 50–51 | `random.randint()` is not designed for security-sensitive PINs. | Replaced it with `secrets.randbelow()` and return a four-digit string. |
| Mutable default argument | Correctness / Medium | 15–20 | `order_log=[]` is shared across calls and may retain data unexpectedly. | Changed the default to `None` and create/use a log only when one is passed in. |
| Bare `except` silently hides errors | Reliability / Medium | 23–27 | `except:` catches broad exceptions and `pass` hides failures, including unexpected errors. | Replaced the try/except with `dict.pop(table_id, None)` and return whether an order was removed. |
| MD5 used for ticket hash | Security practice / Low | 46–47 | MD5 is unsuitable when a modern cryptographic hash is required. A plain table ID hash is not authentication by itself. | Replaced MD5 with SHA-256 and UTF-8 encoding. |
| File opened without a context manager | Quality / Low | 54–57 | A failure during writing could leave the file unclosed. | Used `Path.write_text()` with an explicit encoding. |
| Unused imports and variable | Quality / Low | 6, 31 | `math` is unused; `service_tax` is assigned but never used. | Removed both. |
| Non-PEP 8 function names and formatting | Style / Low | 15, 23, 30, 40 | Several function names use mixed/camel case. | Renamed functions to `snake_case` and reformatted long lines. |
| Direct `main()` call on import | Maintainability / Low | 83 | Importing the module automatically runs the sample operations and writes a file. | Added the `if __name__ == "__main__":` guard. |

## Verification record

Run the three tools on the corrected file and record the actual results from your computer:

```powershell
python -m pylint restaurant_order_system.py
python -m bandit -r restaurant_order_system.py
python -m flake8 restaurant_order_system.py
```

Do not claim that every warning is gone until you have checked the newly generated reports. The exact Pylint score depends on the installed tool version and configuration.
