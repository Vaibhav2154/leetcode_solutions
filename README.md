# LeetCode Solutions

A collection of LeetCode problem solutions implemented in Python, organized by problem categories.

## 📁 Repository Structure

Solutions are organized into the following categories:

```
leetcode_solutions/
├── hashing/          # Hash table and hash map problems
├── math/             # Mathematical problems
├── sliding_window/   # Sliding window technique problems
└── trees/            # Tree data structure problems
```

## 📋 Problems by Category

### Hashing
- **Problem 1** - Two Sum ([Solution](hashing/1.py))
- **Problem 219** - Contains Duplicate II ([Solution](hashing/219.py))
- **Problem 3719** - Longest Balanced Subarray ([Solution](hashing/3719.py))

### Math
- **Problem 7** - Reverse Integer ([Solution](math/7.py))

### Sliding Window
- **Problem 3** - Longest Substring Without Repeating Characters ([Solution](sliding_window/3.py))
- **Problem 219** - Contains Duplicate II ([Solution](sliding_window/219.py))

### Trees
- **Problem 110** - Balanced Binary Tree ([Solution](trees/110.py))
- **Problem 1382** - Balance a Binary Search Tree ([Solution](trees/1382.py))

## 🚀 Usage

Each solution file contains a `Solution` class with the main method(s) to solve the problem. To use any solution:

```python
import importlib.util
import sys

# Load a solution (e.g., Two Sum from hashing/1.py)
spec = importlib.util.spec_from_file_location("solution", "hashing/1.py")
solution_module = importlib.util.module_from_spec(spec)
sys.modules["solution"] = solution_module
spec.loader.exec_module(solution_module)

# Example: Two Sum
solution = solution_module.Solution()
result = solution.twoSum([2, 7, 11, 15], 9)
print(result)  # Output: [0, 1]
```

**Note:** Since solution files are named with problem numbers (e.g., `1.py`), you'll need to use `importlib.util` to load them as module names cannot start with digits in Python.

## 📝 About

This repository contains my personal solutions to various LeetCode problems. The solutions are organized by problem-solving patterns and data structures to make it easier to study and review similar types of problems.

## 🤝 Contributing

This is a personal learning repository, but suggestions and improvements are welcome!

## 📄 License

This project is open source and available for educational purposes.