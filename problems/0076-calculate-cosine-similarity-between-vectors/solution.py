import numpy as np

def cosine_similarity(v1, v2):
    """
    Calculate the cosine_similarity of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The cosine_similarity of the two vectors.
    """
    # Implement your code here
    dot = np.dot(v1, v2)
    
    norm_u = np.sqrt(np.sum(v1 ** 2))
    norm_v = np.sqrt(np.sum(v2 ** 2))

    if norm_u == 0 or norm_v == 0:
        raise ValueError("Zero vector")

    return dot / (norm_u * norm_v)