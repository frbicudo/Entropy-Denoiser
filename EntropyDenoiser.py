# Entropy denoiser by Francisco Bicudo
import numpy as np


def get_entropy(window):
    # Normalize the matrix to obtain probabilities
    prob_mat = window / np.sum(window)

    # Replace 0 by small value to avoid log 0
    prob_mat = np.where(prob_mat > 0, prob_mat, 1e-10)

    # Calculate entropy
    entropy = -np.sum(prob_mat * np.log2(prob_mat))

    # Normalize by the size of the matrix
    entropy /= np.log2(np.size(window))

    return entropy


def denoise(original_matrix, output="", window_height=16, window_width=16, entropy_threshold=0.85,
            magnitude_threshold=0.25):
    matrix = original_matrix.copy()
    for line in range(0, matrix.shape[0], window_height):
        for column in range(0, matrix.shape[1], window_width):
            # window retrieval
            window = original_matrix[line:line + window_height, column:column + window_width]
            # Normalization
            window = (window - np.min(window)) / (np.max(window) - np.min(window))
            # Entropy calculation
            entropy = get_entropy(window)
            if entropy > entropy_threshold:
                # Remove high entropy windows
                window = 0
            else:
                # Apply Magnitude filtering to windows that are kept
                window = np.where(window < magnitude_threshold, 0, window)
            if output == 'entropy':
                # show entropy value instead
                window = entropy
            # Replace old window values with new ones
            matrix[line:line + window_height, column:column + window_width] = window
    if output == 'original':
        # Get original non normalized values
        matrix = np.where(matrix != 0, original_matrix, 0)
    if output == 'mask':
        # Generate binary mask
        matrix = np.where(matrix != 0, 1, 0)
    return matrix
