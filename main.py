# Hailey Clark PA1

def isValidGrid(matrix):
  n = len(matrix)
  quadrant_size = n // 2

  # Sets to store seen values for each quadrant
  quadrants = [set(), set(), set(), set()]
  rows = [set() for _ in range(n)]
  cols = [set() for _ in range(n)]

  # Iterate over each cell in the matrix
  for i in range(n):
    row_values = rows[i]
    col_values = cols[i]

    for j in range(n):
      # Row check
      if matrix[i][j] in row_values:
        return False
      row_values.add(matrix[i][j])

      # Column check
      if matrix[j][i] in col_values:
        return False
      col_values.add(matrix[j][i])

      # Determine which quadrant the current cell belongs to and check for uniqueness
      quadrant_idx = (i // quadrant_size) * 2 + (j // quadrant_size)
      if matrix[i][j] in quadrants[quadrant_idx]:
        return False
      quadrants[quadrant_idx].add(matrix[i][j])

  return True