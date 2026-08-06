# python-dsa

A collection of Python implementations and utilities for common data structures and algorithms. Designed for learning, experimentation, and benchmarking small algorithms.

Features

- Clear, self-contained implementations of algorithms and data structures
- Small utilities such as a `time_decorator` for measuring execution time
- Organized by topic for easy navigation and learning

Requirements

- Python 3.8+

Quick start

1. Clone the repo:
   git clone https://github.com/SyedShamaan2000/python-dsa.git
   cd python-dsa

2. Run a module (example: primality check):
   python3 -m general.is_prime

Using the time_decorator

- Place `time_decorator.py` in the same package or import it by package path.
- Example usage:

```python
from time_decorator import time_decorator

@time_decorator
def is_prime(n: int) -> bool:
    # implementation...
    return True

if __name__ == "__main__":
    print(is_prime(17))
```

Project structure (top-level)

- general/ -- miscellaneous algorithms (e.g., is_prime)
- structures/ -- data-structure implementations
- time_decorator.py -- utility decorator to measure function runtime

Contributing

- Contributions welcome. Open an issue or PR with a short description of the change.
- Follow existing code style and add tests where appropriate.

Contact

- Repo: https://github.com/SyedShamaan2000/python-dsa
