# Island Perimeter

This project implements a function `island_perimeter(grid)` that calculates the perimeter of an island represented in a 2D grid.

## 📌 Problem Description

Given a 2D grid of integers:

- `0` represents **water**
- `1` represents **land**

Each cell is a square of side length `1`. Cells are connected only **horizontally** and **vertically** (not diagonally).

The grid is guaranteed to meet the following constraints:

- The grid is surrounded by water.
- There is only **one island** (or none at all).
- The island has **no lakes** (i.e., no bodies of water that are not connected to the edge of the grid).

The task is to compute and return the **perimeter** of the island.

---

## 🧮 Function Prototype

```python
def island_perimeter(grid: List[List[int]]) -> int:
````

- **Input:** A list of lists of integers (`0` or `1`)
- **Output:** An integer representing the perimeter

---

## ✅ Example

```python
grid = [
  [0, 1, 0, 0],
  [1, 1, 1, 0],
  [0, 1, 0, 0],
  [1, 1, 0, 0]
]

print(island_perimeter(grid))  # Output: 16
```

---

## 🧠 How It Works

For each land cell in the grid:

- Start with a perimeter of 4
- Subtract 1 for each adjacent land cell (up, down, left, right)
- Sum up the adjusted perimeter for all land cells

---

## 🛠 Requirements

- Python 3.x
- No external libraries required

---

## 📁 Files

- `0-island_perimeter.py`: Contains the implementation of `island_perimeter`
- `README.md`: This file

---

## 👨‍💻 Author

- Your Name Here

---

## 📜 License

This project is licensed under the MIT License. See `LICENSE` file for details.
