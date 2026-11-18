def matrixmul(a: list[list[int | float]],
              b: list[list[int | float]]) -> list[list[int | float]] | int:

    if len(a[0]) != len(b):
        return -1

    result = []

    for vector in a:
        row = []

        for i in range(len(b[0])):
            total = 0

            for j in range(len(vector)):
                total += vector[j] * b[j][i]

            row.append(total)

        result.append(row)

    return result