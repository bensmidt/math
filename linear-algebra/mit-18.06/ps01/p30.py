# Author: Benjamin Smidt
# Date: 9 September 2023

import numpy as np
from matplotlib import pyplot as plt


def main():
    # define Markov matrix and initial vector u
    A = np.array([
        [0.8, 0.3],
        [0.2, 0.7]
    ])
    num_iters = 15

    # iteratively multiply matrix on u
    u = np.array([1, 0])
    results = []
    for i in range(num_iters):
        u = A @ u
        results.append(u)

    # plot results
    plt.plot(range(num_iters), results)
    plt.title("Markov Matrix u_0 = (1, 0)")
    plt.xlabel("Iteration")
    plt.ylabel("Value")
    plt.savefig("s21p30a.png")
    plt.show()

    # iteratively multiply matrix on v
    v = np.array([0, 1])
    results = []
    for i in range(num_iters):
        v = A @ v
        results.append(v)

    # plot results
    plt.plot(range(num_iters), results)
    plt.title("Markov Matrix v_0 = (0, 1)")
    plt.xlabel("Iteration")
    plt.ylabel("Value")
    plt.savefig("s21p30b.png")
    plt.show()

    # plot steady state vector
    w = np.array([0.6, 0.4])
    results = []
    for i in range(num_iters):
        w = A @ w
        results.append(w)

    # plot results
    plt.plot(range(num_iters), results)
    plt.title("Markov Matrix w_0 = (0.6, 0.4)")
    plt.xlabel("Iteration")
    plt.ylabel("Value")
    plt.savefig("s21p30c.png")
    plt.show()



if __name__ == "__main__":
    main()
