# NumPy

## What is NumPy?

At its simplest, NumPy (Numerical Python) is a library that allows Python to handle massive amounts of numerical data with extreme speed. While standard Python is great for general logic, it struggles with heavy math; NumPy fixes this by introducing the N-dimensional array (ndarray).

* Basically, it is a library that help the code to using the memories more efficiently and faster runtime.

Example: Filtering scores
* The standard Python way
    ```py
    scores = [72, 95, 50, 84, 91]
    high_scores = []

    for s in scores:
        if s > 80:
            high_scores.append(s)
    ```
* The NumPy way
```py
    import numpy as np

    scores = np.array([72, 95, 50, 84, 91])
#This creates a 'mask' (True/False) and filters instantly
    high_scores = scores[scores > 80]
```

## Linear Algebra

**Linear Algebra** is essentially the mathematics of **arrays**. While basic arithmetic deals with single numbers ($2 + 2 = 4$), Linear Algebra deals with entire sets of numbers (vectors and matrices) at the same time.

* What is it? 
- Vector: A single row or column of data (e.g., the $[x, y, z]$ coordinates of a point)
- Matrix: A table of data (e.g., an Excel spreadsheet or a digital image).A Matrix is what happens when you stack vectors on top of each other. It’s a 2D grid with __Rows__ (horizontal) and __Columns__ (vertical).
- Transformation: Using math to move, rotate, scale, or change those grids.

Example:
A: Digital Images (The Matrix)
- Outside World: 
    When you look at a digital photo, you see a picture.
- Coding World: 
    The computer sees a Matrix where every cell is a number representing a pixel's brightness.
- *Linear Algebra in Action*: 
    When you apply a "Brighten" filter, the code doesn't loop through every pixel. It performs Matrix Addition, adding a value (e.g., $+10$) to the entire grid at once.

B: Recommendation Engines (The Dot Product)
- Outside World: 
    Netflix suggests a movie because "Users who liked Inception also liked The Matrix."
- Coding World: Your interests are stored as a Vector (a list of 1s and 0s for movies you liked).
- *Linear Algebra in Action*: 
    To find a "match," the code calculates the Dot Product between your vector and another user's vector. The higher the resulting number, the closer the match.

C: Navigation & GPS
- Outside World: 
    You rotate a map on your phone to see which way you are facing.
- Coding World: 
    Your location is a vector.
- *Linear Algebra in Action*: 
    To rotate the map, the phone multiplies your location vector by a Rotation Matrix. This instantly calculates the new coordinates for every street and icon on your screen.

  ### 1. Inner or Dot Product of Two n-vectors
To find a Dot Product: 
    __Multiply__ the corresponding components (1st to 1st, 2nd to 2nd) and the __Add__ them up
Mathematically, if $A = [a_1, a_2]$ and $B = [b_1, b_2]$, the dot product is:
            $$A \cdot B = (a_1 \times b_1) + (a_2 \times b_2)$$

In NumPy, we use: 
- `np.inner()`
- `np.dot()`
- `@`
