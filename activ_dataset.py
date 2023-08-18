import numpy as np
import matplotlib.pyplot as plt


def generate_synthetic_series(base_sequence, repetitions=9, noise_max=5):
    """
    Generate a synthetic series by repeating a base sequence and adding noise.
    """
    series = np.tile(base_sequence, repetitions)
    noise = np.random.randint(noise_max, size=series.shape) * 0.01
    return series + noise


def modify_rows(matrix, noise_levels):
    """
    Modify rows of a matrix by adding random noise.
    """
    for row_index, noise_max in noise_levels.items():
        noise = np.random.randint(noise_max, size=matrix.shape[1]) * 0.01
        matrix[row_index, :] += noise
    return matrix


def main():
    # Initial sequence: 5 days of high activity and 2 days of low activity
    base_sequence = np.zeros(7)
    base_sequence[:5] = 1

    # Generate synthetic series
    s = generate_synthetic_series(base_sequence)

    # Duplicate the series several times vertically
    s = np.tile(s, (4, 1))

    # Apply shifts and noise to rows
    shifts = {i: i * 2 for i in range(15)}
    for row, shift_amount in shifts.items():
        s[row, :] = np.roll(s[0, :], shift_amount)

    noise_levels = {
        1: 9,
        2: 15,
        3: 50,
        4: 20,
        6: 5,
        8: 40
    }
    s = modify_rows(s, noise_levels)

    # Create a linearly increasing y sequence
    y = np.linspace(0.0001, s.shape[1] * 0.0001, s.shape[1])
    y = np.reshape(y, (1, s.shape[1]))

    # Modify rows of s using y and a multiplier
    for r in range(1, 10):
        s[r, :] += y
        s[r, :] *= r

    # Extract a submatrix from s
    X = s[:10, :]

    # Save X to a CSV file
    np.savetxt('activity.csv', X, delimiter=',')

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(s[0, :50], label='s[0]')
    for r in range(10):
        plt.plot(X[r, 3400:3500], label=f'X[{r}]')
    plt.legend()
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.show()


if __name__ == "__main__":
    main()