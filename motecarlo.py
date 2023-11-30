import numpy as np
from matplotlib import pyplot as plt

def metropolis_integral(delta, N=3000, N0=0):
    """
    Metropolis algorithm to estimate the integral in Exercise 3.1 a.

    Parameters:
    delta (float): Parameter delta for the trial point generation.
    N (int): Number of points to generate.
    N0 (int): Number of initial points to skip.

    Returns:
    float: Estimated integral value.
    """
    def target_distribution(x):
        return np.exp(-x) if x >= 0 else 0

    x = 0  # start at x = 0
    integral_values = []

    for i in range(N):
        x_trial = x + np.random.uniform(-delta, delta)
        w = target_distribution(x_trial) / target_distribution(x)

        if w >= np.random.rand():
            x = x_trial  # accept the new point

        if i >= N0:
            integral_values.append(x)

    # Calculate the integral value
    integral_estimate = np.mean([x for x in integral_values if x >= 0])
    return integral_values, integral_estimate






# Exact value of the integral (assuming known for demonstration)
exact_value = 1  # Replace with the actual exact value


deltas = np.linspace(0.01, 10, 50)
amount_of_runs_per_delta = 100


RMS_average = []
RMS_difference = []
STDEs = []

for delta in deltas: 
    stdes = []
    square_diffs = []
    for i in range(amount_of_runs_per_delta): 
        x, estimate = metropolis_integral(delta)

        var = np.std(x, ddof = 1)
        stde = np.sqrt(var / len(x))
        stdes.append(stde)


        square_diffs.append((estimate - exact_value)**2)


    RMS_average.append(np.mean(np.square(stdes)))
    RMS_difference.append(np.sqrt(np.mean(square_diffs)))
    STDEs.append(stde)






plt.figure(figsize=(12, 6))

plt.title('Different errors as a function of delta for metropolis integral')
plt.plot(deltas, RMS_difference, label='RMS Difference', color='red')
plt.plot(deltas, RMS_average, label='RMS averages', color='blue')
plt.plot(deltas, STDEs, label='Standarderrors', color='black')
plt.xlabel('Delta')
plt.ylabel('errors')
plt.legend()
plt.show()