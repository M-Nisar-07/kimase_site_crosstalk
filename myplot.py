
import matplotlib.pyplot as plt

def get_plot(pvl, cdf, k , type):
    plt.plot(pvl, cdf, marker='.', linestyle='none')

    plt.xlabel('P-values')
    plt.ylabel('Cumulative Probability')
    plt.title('Cumulative Distribution Function (CDF) of P-values')
    plt.grid(True)
    plt.savefig(f'{k}_{type}_plot.svg',format='svg')


