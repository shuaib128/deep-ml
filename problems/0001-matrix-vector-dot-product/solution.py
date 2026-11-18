def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # Return a list where each element is the dot product of a row of 'a' with 'b'.
    # If the number of columns in 'a' does not match the length of 'b', return -1.
    if len(a) != len(b):
        return -1
    
    result = []

    for vector in a:
        sum = 0

        for i in range(len(vector)):
            sum += vector[i] * b[i]
        
        result.append(sum)

    return result