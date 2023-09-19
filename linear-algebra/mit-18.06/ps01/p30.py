# Author: Benjamin Smidt
# Date: 9 September 2023

import numpy as np
from matplotlib import pyplot as plt

def main():
    A = [[0.8, 0.3], [0.2, 0.7]]
    u = [1, 0]
    results = []

    for i in range(7):
        u = A @ u
        results.append(u)

    plt.plot
    


if __name__ == "__main__":
    print main()