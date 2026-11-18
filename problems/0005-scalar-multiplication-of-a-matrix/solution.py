def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
    for vector in matrix:
        for i in range(len(vector)):
            vector[i] *= scalar

    return(matrix)