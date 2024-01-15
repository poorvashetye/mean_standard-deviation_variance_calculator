import numpy as np


def calculate(number):
  if len(number) != 9:
    raise ValueError("List must contain exact 9 numbers")

  matrix = np.array(number).reshape(3, 3)
  results = {
      'mean': [
          list(matrix.mean(axis=0)),
          list(matrix.mean(axis=1)),
          float(matrix.mean())
      ],
      'variance': [
          list(matrix.var(axis=0)),
          list(matrix.var(axis=1)),
          float(matrix.var())
      ],
      'standard deviation': [
          list(matrix.std(axis=0)),
          list(matrix.std(axis=1)),
          float(matrix.std())
      ],
      'max': [
          list(matrix.max(axis=0)),
          list(matrix.max(axis=1)),
          float(matrix.max())
      ],
      'min': [
          list(matrix.min(axis=0)),
          list(matrix.min(axis=1)),
          float(matrix.min())
      ],
      'sum': [
          list(matrix.sum(axis=0)),
          list(matrix.sum(axis=1)),
          float(matrix.sum())
      ]
  }

  return results


number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
results = calculate(number)
print(results)
